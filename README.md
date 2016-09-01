# mkrg

#mkrgBuild.cpp
Starts with guassian distirbution and iterates mkrg for a give number of steps. Then saves all data to file.

#mkrgBC.cpp (not currently used)
Reads in data from mkrgBuild.cpp to calculate boundary condition. Caluclates BC for every system size possible given data and then saves the values to file.

#mkrgBCTrack.cpp
Reads in data from mkrgBuild.cpp to calculate BC. First creates array with a large number of disorder realizations (tracks) and then calculates the BC for every system size for every track. Saves this to file.

#mkrgBCTrackPlot.py
Reads in datat from mkrgBCTrack.cpp. First calculates the correlation function for every track and then finds the rate of decay of that correlation function. This quantifies the rate that the BC approaches its final value. Also plots the correlation \ and related values.

#data/
Contains all sored data

#out/
Contains all figures

#transfer/
Simple folder to transfer from server with scp


##0tmkrg

First generates 0t distribution like normal mkrg code but then uses 0t relations only to calculate boundary condition. Also scalles the distribution by lambda for different bond orders instead of saving every distribution. 

###mkrgBuilder.py
Starts with gaussian distribution and iterates on mkrg into the 0t regieme. Calculates scaling factor, lambda, and generates large finial distribution to save to file. Works for either diamond or necklace distributions.

###mkrgBC.py
Reads distribution from mkrgBuilder.py to create disorder realiations and claculate the boundary condition as a function of system size. Then calculates a correlation functon off the BC values to quantify the rate at which the BC approaches its final value.

