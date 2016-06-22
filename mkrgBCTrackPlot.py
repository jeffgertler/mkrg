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
print(J)

print("Plotting")
for i in range(100):
    pl.plot(range(len(J[i])), J[i])
pl.show()
