
all:
	

build:
	g++ -c mkrgBuild.cpp
	gcc -c mkrgLibrary.c
	g++ -o mkrgBuild mkrgBuild.o mkrgLibrary.o
	./mkrgBuild 1 2 3.1234 n
