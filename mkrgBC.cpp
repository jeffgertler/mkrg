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

    int sub_system_size = 0;
    int super_system_size = atoi(argv[5]);

    // Setup file reading
    char file_name[80];
    sprintf(file_name, "data/mkrg_L=%i_N=%i_J0=%.0lf_distType=%c.txt", L, N, J0, dist_type);
    printf("Reading from: %s\n", file_name);
    FILE *file = fopen(file_name, "r");

    // Initialize bond array
    double *J = (double *) malloc(L * N * sizeof(double));


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
            fscanf(file, "%lf", &J[l*N + n]);
        }
    }
  
    // Setup file writing
    sprintf(file_name, "data/mkrgBC_L=%i_N=%i_J0=%.0lf_distType=%c.txt", L, N, J0, dist_type);
    printf("Writing to: %s\n", file_name);
    file = fopen(file_name, "w");

    // Calcualte BC
    std::random_device rd; // obtain a random number from hardware
    std::mt19937 eng(rd()); // seed the generator
    std::uniform_int_distribution<int> uni(0, N-1);
    double J_net[N];
    double J_temp;
    int progress_counter = 0;
    int count = 0;
    for(c=0; c<N; c++){
        if(c%(N/10) == 0){
            printf("%i%% complete\n", ++progress_counter*10);
        }
        J_net[c] = 0;
        for(i=0; i<3; i++){
            J_net[c] += J[super_system_size*N + uni(eng)]; // J_net += 3J_L
        }
        for(l=super_system_size-1; l>=sub_system_size; l--){
            count=0;
            J_temp = 0;
            for(i=0; i<4; i++){
                J_temp += J[l*N + uni(eng)]; // 4 J_l
            }
            //if(fabs(series(J_net[c], J_temp, J0)) > fabs(J_net[c])){
            //    count++;
            //}
            printf("%f, %f, %f\n", J_net[c], J_temp, series(J_net[c], J_temp, J0));
            J_net[c] = series(J_net[c], J_temp, J0);
            for(i=0; i<3; i++){
                J_net[c] += J[l*N + uni(eng)]; // J_net += 3J_l
            }
        }
        fprintf(file, "%f\t", J_net[c]);
    }
    printf("%i/%i\n", count, N);
    
    fclose(file);
    
    return 0;
    
}
