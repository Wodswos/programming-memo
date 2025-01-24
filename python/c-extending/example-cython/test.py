import time
import fib_native
import fib_cython

# compile command
# cp fib_native.py fib_cython.py && cythonize -i fib_cython.py && rm -f fib_cython.py fib_ctyhon.c

start_time = time.time()
result = fib_cython.fib(40)  # 计算斐波那契数列的第 40 项
end_time = time.time()
print(f"Cython 计算结果: {result}")
print(f"Cython 耗时: {end_time - start_time:.4f} 秒")

start_time = time.time()
result = fib_native.fib(40)  # 计算斐波那契数列的第 40 项
end_time = time.time()
print(f"Python 计算结果: {result}")
print(f"Python 耗时: {end_time - start_time:.4f} 秒")
