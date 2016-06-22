import numpy as np
import matplotlib.pyplot as pl
import sys
import math

L = int(sys.argv[1])
N = int(sys.argv[2])
J0 = float(sys.argv[3])
dist_type = sys.argv[4]

print("Reading file into python")
file_name = "mkrgBC_L=" + str(L) + "_N=" + str(N) + "_J0=" + str(int(J0)) + "_distType=" + dist_type
J = np.loadtxt("data/" + file_name + ".txt")

print(np.mean(J), np.var(J))

print("Plotting")
a, bins = np.histogram(J, bins= np.linspace(-6, 6, 100))
#pl.plot(bins[:-1], np.sqrt(-np.log(a/float(a[50]))))
pl.plot(bins[:-1], a)
pl.show()


'''
pl.hist(J, bins=N/1000)
pl.show()
'''
