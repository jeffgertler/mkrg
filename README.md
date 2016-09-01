# mkrg

0tmkrg

First generates 0t distribution like normal mkrg code but then uses 0t relations only to calculate boundary condition. Also scalles the distribution by lambda for different bond orders instead of saving every distribution. 

mkrgBuilder.py
Starts with gaussian distribution and iterates on mkrg into the 0t regieme. Calculates scaling factor, lambda, and generates large finial distribution to save to file. Works for either diamond or necklace distributions.

mkrgBC.py
Reads distribution from mkrgBuilder.py to create disorder realiations and claculate the boundary condition as a function of system size. Then calculates a correlation functon off the BC values to quantify the rate at which the BC approaches its final value.

