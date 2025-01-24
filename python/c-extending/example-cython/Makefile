test_fb: fib_native.py
	cp fib_native.py fib_cython.py 
	cythonize -i fib_cython.py
	rm -f fib_cython.py fib_cython.c && python3 test.py

clean:
	rm -f fib_cython.cpython-*

.PHONY: clean