import numpy as np
import matplotlib.pyplot as pl
import math


def recN0T(K):
    return .5 * (abs(K[0] + K[1] + K[2] + K[3] + K[4] + K[5] + K[6] + K[7])
               - abs(K[0] + K[1] + K[2] + K[3] - K[4] - K[5] - K[6] - K[7]))

def recN(K, MAX_VALUE):
    if(abs(K[0] + K[1] + K[2] + K[3] + K[4] + K[5] + K[6] + K[7]) > MAX_VALUE
    	or abs(K[0] + K[1] + K[2] + K[3] - K[4] - K[5] - K[6] - K[7]) > MAX_VALUE):
    	return recN0T(K)
    else:
    	return .5 * math.log(math.cosh(K[0] + K[1] + K[2] + K[3] + K[4] + K[5] + K[6] + K[7])
               			  / math.cosh(K[0] + K[1] + K[2] + K[3] - K[4] - K[5] - K[6] - K[7]))

def series(K1, K2, MAX_VALUE):
	if(abs(K1 + K2) > MAX_VALUE or abs(K1 - K2) > MAX_VALUE):
		return .5 * (abs(K1 + K2) - abs(K1 - K2))
	else:
		return .5 * math.log(math.cosh(K1 + K2) / math.cosh(K1 - K2))

def recD0T(K):
    return .5 * (abs(K[0] + K[1]) - abs(K[0] - K[1])
    		   + abs(K[2] + K[3]) - abs(K[2] - K[3])
    		   + abs(K[4] + K[5]) - abs(K[4] - K[5])
    		   + abs(K[6] + K[7]) - abs(K[6] - K[7]))

def recD(K, MAX_VALUE):
	return (series(K[0], K[1], MAX_VALUE) + series(K[2], K[3], MAX_VALUE)
		  + series(K[4], K[5], MAX_VALUE) + series(K[6], K[7], MAX_VALUE))


N = 100000
N_burn = 100000
L = 30
var_K0 = 5.
MAX_VALUE = 20.
mkrg_type = "D"



K = np.zeros((L, N_burn))
K[0] = np.random.normal(0., var_K0, N_burn)

''' Burn into 0t regieme '''
for l in range(L-1):
	print(str(l+1) + '/' + str(L) + ', var = ' + str(np.var(K[l])))
	for n in range(N_burn):
		if(mkrg_type == "N"):
			K[l+1, n] = recN(K[l, np.random.randint(0, N_burn-1, size=8)], MAX_VALUE)
		if(mkrg_type == "D"):
			K[l+1, n] = recD(K[l, np.random.randint(0, N_burn-1, size=8)], MAX_VALUE)

''' Calculate lam by iterating at 0t '''
K_temp = np.zeros(N_burn)
lam = np.zeros(100)
for i in range(100):
	print(i)
	for n in range(N_burn):
		if(mkrg_type == "N"):
			K_temp[n] = recN0T(K[L-1, np.random.randint(0, N_burn-1, size=8)])
		elif(mkrg_type == "D"):
			K_temp[n] = recD0T(K[L-1, np.random.randint(0, N_burn-1, size=8)])
	lam[i] = np.var(K_temp) / np.var(K[L-1])
print(np.mean(lam), np.std(lam))

''' Build final distribution '''
K_final	= np.empty(N)
for n in range(N):
	if(mkrg_type == "N"):
		K_final[n] = recN0T(K[L-1, np.random.randint(0, N_burn-1, size=8)])
	elif(mkrg_type == "D"):
		K_final[n] = recD0T(K[L-1, np.random.randint(0, N_burn-1, size=8)])

''' Resize K_final to var=1 '''
K_final *= 1./np.sqrt(np.var(K_final))


np.savetxt("data/0tmkrg_N=" + str(N) + "_mkrg=" + str(mkrg_type) + ".txt", 
			np.append(np.array([np.mean(lam)]), K_final))

