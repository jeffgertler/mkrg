#include <stdio.h>
#include <math.h>
#include "mkrgLibrary.h"


double rec3d(double *J){
    return .5 * log(cosh(J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7])
                  / cosh(J[0]+J[1]+J[2]+J[3]-J[4]-J[5]-J[6]-J[7]));
}

double rec3d0t(double *J){
    return .5 * (fabs(J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7])
               - fabs(J[0]+J[1]+J[2]+J[3]-J[4]-J[5]-J[6]-J[7]));
}

int check0t(double *J, double cutoff){
    if(fabs(J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]) > cutoff 
         || fabs(J[0]+J[1]+J[2]+J[3]-J[4]-J[5]-J[6]-J[7]) > cutoff){
        return 1;
    } else {
        return 0;
    }
}

double series(double J1, double J2, double cutoff){
    if(fabs(J1+J2) > cutoff || fabs(J1-J2) > cutoff){
        return .5 * (fabs(J1+J2) - fabs(J1-J2));
    } else {
        return .5 * log(cosh(J1+J2) / cosh(J1-J2));
    }
}
