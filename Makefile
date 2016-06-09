
all:
	

build:
	g++ -c mkrgBuild.cpp
	gcc -c mkrgLibrary.c
	g++ -o mkrgBuild mkrgBuild.o mkrgLibrary.o
	./mkrgBuild
