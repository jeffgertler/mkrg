L= 10
N = 100000
J0 = 20
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
	./mkrgBC $(L) $(N) $(J0) $(dist_type)
	python mkrgBCPlot.py $(L) $(N) $(J0) $(dist_type)

