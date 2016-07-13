import numpy as np
import matplotlib.pyplot as pl
import sys
import math

def correlation(J_track, n):
    return (math.tanh(J_track[n]) - math.tanh(J_track[-1]))/(math.tanh(J_track[0]) - math.tanh(J_track[-1]))




L = int(sys.argv[1])
N = int(sys.argv[2])
J0 = float(sys.argv[3])
dist_type = sys.argv[4]

print("Reading file into python")
file_name = "mkrgBCTrack_L=" + str(L) + "_N=" + str(N) + "_J0=" + str(int(J0)) + "_distType=" + dist_type
J = np.loadtxt("data/" + file_name + ".txt")

print(J.shape)

sub_system_size = 0


corr = np.zeros((N, L-sub_system_size))
for n in range(N):
    for l in range(L-sub_system_size):
        corr[n, l] = correlation(J[n], l)

print(np.mean(corr, axis=0))
pl.plot(range(sub_system_size, L), np.mean(corr, axis=0), 'k')
#pl.plot(range(sub_system_size, L), np.std(corr, axis=0), 'b')
pl.show()

'''
J_cross = np.zeros_like(J)
for n in range(N):
    for l in range(1, L-sub_system_size):
        #if(J[n, l-1] * J[n, l] < 0):
        if(J[n, l-1] * J[n, l] < 0 and abs(J[n, l-1] - J[n, l]) > 18.8):
            J_cross[n,l] += 1

J_cross_frac = np.zeros(L)
for l in range(1, L-sub_system_size):
    temp = np.sum(J_cross[:,l:], axis=1)
    J_cross_frac[l] = (1.0 + len(temp[temp>0])) / N

print("Plotting")
for n in range(100):
    #if(np.sum(J_cross[n, 7:]>0)):
    pl.hist(J[:,0], bins=100)
pl.show()
pl.clf()

pl.plot(range(sub_system_size, len(J_cross_frac)+sub_system_size), np.log(J_cross_frac))
pl.show()
'''
