import numpy as np
import matplotlib.pyplot as pl
import sys
import math

def correlation(J_track, n):
    #return (math.tanh(J_track[n]) - math.tanh(J_track[-1]))/(math.tanh(J_track[0]) - math.tanh(J_track[-1]))
    return abs(math.tanh(J_track[n]) - math.tanh(J_track[-1]))




L = int(sys.argv[1])
N = int(sys.argv[2])
J0 = float(sys.argv[3])
dist_type = sys.argv[4]

file_name = "mkrgBCTrack_L=" + str(L) + "_N=" + str(N) + "_J0=" + "{:.5f}".format(J0) + "_distType=" + dist_type
print("Reading " + file_name + " into python")
J = np.loadtxt("data/" + file_name + ".txt")


J = J.reshape(L, N, L)
print(J.shape)



log_slope = np.zeros(L-5)
initial = np.zeros_like(log_slope)

corr = np.zeros((N, L))
for sub_system_size in range(L-5):
    print("itteration " + str(sub_system_size))
    for n in range(N):
        for l in range(L):
            corr[n, l] = correlation(J[sub_system_size, n], l)
    corr_ave = np.mean(corr, axis=0)
    log_corr = np.log(corr_ave)
    log_slope[sub_system_size] = (log_corr[sub_system_size] - log_corr[sub_system_size+4]) / 4
    initial[sub_system_size] = corr_ave[sub_system_size] 
    pl.plot(range(sub_system_size, L), log_corr[sub_system_size:L]);
pl.show()
pl.clf()

print(log_slope)
print(np.mean(log_slope), np.std(log_slope))

pl.plot(range(L-5), log_slope)
pl.show()
pl.clf()
pl.plot(range(L-5), initial)
pl.show()
pl.clf()



'''
print("sub_system_variance: " + str(np.var(J[0])))
print("inital value: " + str(values[0]))
print("log slope: " + str((values[0]-values[5])/5))
pl.plot(range(sub_system_size, L), np.log(np.mean(corr, axis=0)), 'k')
#pl.plot(range(sub_system_size, L), np.std(corr, axis=0), 'b')
pl.show()
pl.clf()
'''


'''
for n in range(100):
    pl.plot(range(L), np.tanh(J[n]))
pl.show()
'''




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
