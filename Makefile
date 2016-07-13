L= 20
N = 5000000
J0 = 10
dist_type = n


all:
	

build:
	g++ -c mkrgBuild.cpp
	gcc -c mkrgLibrary.c
	g++ -o mkrgBuild mkrgBuild.o mkrgLibrary.o
	./mkrgBuild $(L) $(N) $(J0) $(dist_type)

plot:
	python mkrgPlot.py $(L) $(N) $(J0) $(dist_type)

bc:
	g++ -c mkrgBC.cpp
	gcc -c mkrgLibrary.c
	g++ -o mkrgBC mkrgBC.o mkrgLibrary.o
	./mkrgBC $(L) $(N) $(J0) $(dist_type) 0 
	python mkrgBCPlot.py $(L) $(N) $(J0) $(dist_type)

bctrack:
	g++ -c mkrgBCTrack.cpp
	gcc -c mkrgLibrary.c
	g++ -o mkrgBCTrack mkrgBCTrack.o mkrgLibrary.o
	./mkrgBCTrack $(L) $(N) $(J0) $(dist_type)
	python mkrgBCTrackPlot.py $(L) $(N) $(J0) $(dist_type)

