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

    // Input arguments
    int L = atoi(argv[1]);
    int N = atoi(argv[2]);
    double J0 = atof(argv[3]);
    char dist_type = (char) argv[4][0];
    int mkrg_num = 8; // Number of bonds per mkrg iteration

    // Setup file writing
    char file_name[80];
    sprintf(file_name, "data/mkrg_L=%i_N=%i_J0=%.0lf_distType=%c.txt", L, N, J0, dist_type);
    printf("%s\n", file_name);
    FILE *file = fopen(file_name, "w");
    fprintf(file, "%i\t%i\t%.0lf\t%c\n", L, N, J0, dist_type);

    // Initialize bond array
    double *J = (double *) malloc(L * N * sizeof(double));
   
    // Setup normal distribution
    //std::default_random_engine generator;
    std::random_device rd; // obtain a random number from hardware
    std::mt19937 eng(rd()); // seed the generator
    //if(dist_type == 'n'){
        std::normal_distribution<double> distribution(0., 1.);
    //}
    for(n=0; n<N; n++){
        J[n] = distribution(eng);
    }


    // Iterate MKRG
    std::uniform_int_distribution<int> uni(0, N-1);
    //int *a = (int *) malloc(8 * sizeof(double));
    double *J_temp = (double *) malloc(mkrg_num * sizeof(double));
    for(l=0; l<L-1; l++){
        printf("itteration: %i\n", l);
        for(n=0; n<N; n++){
            for(i=0; i<mkrg_num; i++){
                J_temp[i] = J[l*N + uni(eng)];
            }
            if(check0t(J_temp, J0)){
                J[(l+1)*N + n] = rec3d0t(J_temp);
            } else {
                J[(l+1)*N + n] = rec3d(J_temp);
            }
        }
    }

    // Printing to file
    for(l=0; l<L; l++){
        for(n=0; n<N; n++){
            fprintf(file, "%f", J[l*N + n]);
            if(n<N-1){
                fprintf(file, "\t");
            }
        }
        fprintf(file, "\n");
    }

    
    fclose(file);
    
    return 0;
    
}
