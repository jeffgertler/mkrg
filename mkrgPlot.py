import numpy as np
import matplotlib.pyplot as pl
import math
import sys

L = int(sys.argv[1])
N = int(sys.argv[2])
J0 = float(sys.argv[3])
dist_type = sys.argv[4]

text = np.loadtxt("mkrg_L=" + str(L) + "_N=" + str(N) + "_J0=" + str(J0) + dist_type = sys.argv[4]
               skiprows=1)

print(text)
