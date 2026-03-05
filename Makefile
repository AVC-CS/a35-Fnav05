all: clean test
programtest: tests.cpp 
	g++ -fsanitize=address --std=c++17 tests.cpp -o programtest 
	# g++ --std=c++17 tests.cpp -o programtest 
test: programtest 
	./programtest
clean:
	rm -rf programtest a.out *.o main .pytest_cache
	rm -rf __pycache__
	rm -rf *.dSYM
	rm -f result*.txt
