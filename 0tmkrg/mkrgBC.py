import numpy as np
import matplotlib.pyplot as pl
import math


def series(K1, K2):
	return .5 * (abs(K1 + K2) - abs(K1 - K2))

def correlation(K, K_inf):
	return abs(math.tanh(K) - math.tanh(K_inf))

''' Constants '''
N = 100000
L = 20
num_traces = 10000
mkrg_type = "D"

''' Read in 0t distribution '''
print("reading from data/0tmkrg_N=" + str(N) + "_mkrg=" + str(mkrg_type) + ".txt")
K = np.loadtxt("data/0tmkrg_N=" + str(N) + "_mkrg=" + str(mkrg_type) + ".txt")
lam = np.copy(K[0])
K = K[1:]

'''
pl.hist(K, bins = 100)
pl.show()
pl.clf()
'''

print("lam = " + str(lam))
yint = np.zeros(20)
exponent = np.zeros(20)

''' itterate 20 times to generate std of yint and exponnent '''
for i in range(20):
	print(str(i) + "/" + str(20))
	K_traces = np.zeros((num_traces, L, 7))

    ''' Fill in array containing the disorder realization to calculate the bc with '''
	for n in range(num_traces):
		for l in range(L):
			K_traces[n, l] = K[np.random.randint(0, N-1, 7)] * (lam ** (l))

	bc = np.zeros((num_traces, L))
	corr = np.zeros_like(bc)

	status = 0
    ''' Neclace Code '''
	if(mkrg_type == "N"):
		for n in range(num_traces):
			'''
			if(n%(num_traces/10) == 0): 
				print(str(status) + "%")
				status+=10
			'''
			for l in range(L):
				bc[n, l] = np.sum(K_traces[n, l, 0:3])
				for ss in range(l, 0, -1):
					bc[n, l] = series(bc[n, l], np.sum(K_traces[n, ss, 0:4]))
					bc[n, l] += np.sum(K_traces[n, ss, 4:7])
			for l in range(L):
				corr[n, l] = correlation(bc[n, l], bc[n, L-1])
    ''' Diamond code '''
	if(mkrg_type == "D"):
		for n in range(num_traces):
			'''
			if(n%(num_traces/10) == 0): 
				print(str(status) + "%")
				status+=10
			'''
			for l in range(L):
				for ss in range(l, 0, -1):
					bc[n, l] += (series(K_traces[n, ss, 0], K_traces[n, ss, 1])
							   + series(K_traces[n, ss, 2], K_traces[n, ss, 3])
							   + series(K_traces[n, ss, 4], K_traces[n, ss, 5]))
					bc[n, l] = series(bc[n, l], K_traces[n, ss, 6])
			for l in range(L):
				corr[n, l] = correlation(bc[n, l], bc[n, L-1])

    ''' Calculate the yint and exponnent from correlation values '''
	corr_mean = np.mean(corr, axis=0)
	yint[i] = corr_mean[0]
	exponent[i] = (np.log(corr_mean[5]) - np.log(corr_mean[0]))/5
	#print(corr_mean[0], (np.log(corr_mean[5]) - np.log(corr_mean[0]))/5)

print(np.mean(yint), np.std(yint))
print(np.mean(exponent), np.std(exponent))



