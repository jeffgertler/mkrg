import numpy as np
import matplotlib.pyplot as pl
import sys

L = int(sys.argv[1])
N = int(sys.argv[2])
J0 = float(sys.argv[3])
dist_type = sys.argv[4]

file_name = "mkrg_L=" + str(L) + "_N=" + str(N) + "_J0=" + "{:.5f}".format(J0) + "_distType=" + dist_type
text = np.loadtxt("data/" + file_name + ".txt", skiprows=1, delimiter='\t')

'''
for l in range(L):
    print(str(l) + "/" + str(L))
    print(np.var(text[l]))
    pl.hist(text[l], bins = (N/100))
    pl.savefig("out/" + file_name + "_" + str(l) + ".png")
    pl.clf()
'''
print(text.shape)
print(np.var(text, axis=1))

pl.plot(range(L), np.var(text, axis=1))
pl.show()
