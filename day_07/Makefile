day_07: day_07.o File.o
	g++ day_07.o File.o -o day_07

day_07.o: File.o
	g++ -g -c --std=c++17 day_07.cpp File.o

File.o:
	g++ -g -c --std=c++17 File.cpp

clean:
	rm File.o day_07.o day_07
