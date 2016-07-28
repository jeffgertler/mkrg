#include <stdlib.h>
#include <stdio.h>
#include <random>
#include <typeinfo>

#include "mkrgLibrary.h"


int main(int argc, char* argv[]){
    // Loop counter
    int i;
    int l;
    int n;
    int c;

    // Input arguments
    int L = atoi(argv[1]);
    int N = atoi(argv[2]);
    double J0 = atof(argv[3]);
    char dist_type = (char) argv[4][0];
    int mkrg_num = 8; // Number of bonds per mkrg iteration



    // Setup file reading
    char file_name[80];
    sprintf(file_name, "data/mkrg_L=%i_N=%i_J0=%.5lf_distType=%c.txt", L, N, J0, dist_type);
    printf("Reading from: %s\n", file_name);
    FILE *file = fopen(file_name, "r");

    // Initialize bond array
    double *J_data = (double *) malloc(L * N * sizeof(double));


    // Read in the file
    // Kill off the header (there has to be a better way to do this)
    char buff[300];
    fscanf(file, "%s", buff);
    printf("%s, ", buff);
    fscanf(file, "%s", buff);
    printf("%s, ", buff);
    fscanf(file, "%s", buff);
    printf("%s, ", buff);
    fscanf(file, "%s", buff);
    printf("%s\n", buff);

    // Fill J
    for(l=0; l<L; l++){
        for(n=0; n<N; n++){
            fscanf(file, "%lf", &J_data[l*N + n]);
        }
    }

    std::random_device rd; // obtain a random number from hardware
    std::mt19937 eng(rd()); // seed the generator
    std::uniform_int_distribution<int> uni(0, N-1);
 
    // Initalize relization matrix
    double *J = (double *) malloc(N * L * 7 * sizeof(double));
    for(c=0; c<N; c++){
        for(l=0; l<L; l++){
            for(i=0; i<7; i++){
                J[c*(L*7) + l*7 + i] = J_data[l*N + uni(eng)];
            }
        }
    }

    // Setup file writing
    sprintf(file_name, "data/mkrgBCTrack_L=%i_N=%i_J0=%.5lf_distType=%c.txt", L, N, J0, dist_type);
    printf("Writing to: %s\n", file_name);
    file = fopen(file_name, "w");

    // Calcualte BC
    double J_net;
    double J_temp;
    int sub_system_size;
    int super_system_size;
    int progress_counter = 0;
    // Itterate through the walkers
    for(i=0; i<L; i++){
        sub_system_size = i;
        for(c=0; c<N; c++){
            if(c%(N*L/10) == 0){
                printf("%i%% complete\n", ++progress_counter*10);
            }
            // Itterate through the system sizes (there are a ton of magic numbers here, its mainly just pulling those 7
            // values per l from J)
            for(super_system_size=0; super_system_size<sub_system_size; super_system_size++){
                fprintf(file, "%f\t", 0.0);
            }
            for(super_system_size=sub_system_size; super_system_size<L; super_system_size++){
                J_net = J[c*(L*7) + super_system_size*7] + J[c*(L*7) + super_system_size*7 + 1]
                       + J[c*(L*7) + super_system_size*7 + 2]; // J_net = 3J_L
                for(l=super_system_size-1; l>=sub_system_size; l--){
                    J_temp = J[c*(L*7) + l*7] + J[c*(L*7) + l*7 + 1]
                           + J[c*(L*7) + l*7 + 2] + J[c*(L*7) + l*7 + 3]; // 4 J_l
                    J_net = series(J_net, J_temp, J0); // J_net:4J_l
                    J_net += J[c*(L*7) + l*7 + 4] + J[c*(L*7) + l*7 + 5] + J[c*(L*7) + l*7 + 6]; // J_net += 3J_l
                }
                fprintf(file, "%f\t", J_net);
            }
            fprintf(file, "\n");
        }
    }

    
    fclose(file);
    
    return 0;
    
}
