#include <stdlib.h>
#include <stdio.h>
#include <random.h>

#include "mkrgLibrary.h"


int main(int argc, char* argv[]){
    int L = argv[1][0] - '0';
    int N = argv[2][0] - '0';
    double J0 = atof(argv[3]);
    char dist_type = (char) argv[4][0];

    double *J = (double *) malloc(L * N * sizeof(double));
   
    std::default_random_engine generator;
    

    double *a = (double *) malloc(8 * sizeof(double));
    int i;
    for(i=0; i<8; i++){
        a[i] = (double) 1;
    }
    printf("%f\n", rec3d(a));
    printf("%f\n", rec3d0t(a));
    return 0;
    
}
