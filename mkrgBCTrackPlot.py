import numpy as np
import matplotlib.pyplot as pl
import sys
import math

L = int(sys.argv[1])
N = int(sys.argv[2])
J0 = float(sys.argv[3])
dist_type = sys.argv[4]

print("Reading file into python")
file_name = "mkrgBCTrack_L=" + str(L) + "_N=" + str(N) + "_J0=" + str(int(J0)) + "_distType=" + dist_type
J = np.loadtxt("data/" + file_name + ".txt")

J_cross = np.zeros_like(J);
for n in range(N):
    for l in range(1, L):
        if(J[n, l-1] * J[n, l] < 0):
            J_cross[n,l] += 1

J_cross1 = np.sum(J_cross[:,7:], axis=1)
print(len([J_cross1>0]))

print("Plotting")
count = 0
for n in range(N):
    if(np.sum(J_cross[n, 7:]>0)):
        pl.plot(range(L), J[n])
        count+=1
print(count)
pl.show()
