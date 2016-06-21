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
text = np.loadtxt("data/" + file_name + ".txt")

print(str((1.0 * len(text[text == float('inf')])/N)*100) + '% inf')
print(str((1.0 * len(text[text == -float('inf')])/N)*100) + '% -inf')
print(str((1.0 * len(text[np.isnan(text)])/N)*100) + '% nan')

J_temp = text[text != float('inf')]
J_temp = J_temp[J_temp != -float('inf')]
J = J_temp[np.invert(np.isnan(J_temp))]


print("Plotting")
pl.hist(J, bins=N/1000)
pl.show()
