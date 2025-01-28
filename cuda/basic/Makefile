NVCC  = nvcc

CFLAGS = -O2 -std=c++11

# CUDA Architecture Version
ARCH = sm_80  # corresponding to RXT3080 / A100, don't use v100.

# target

test_async_engine: test_async_engine.cu
	$(NVCC) $(CFLAGS) -arch=$(ARCH)	-o $@ $<

matmul: matmul.cpp matmul.cu
	$(NVCC) $(CFLAGS) matmul.cu -arch=$(ARCH) -o cuda_matmul
	g++ $(CFLAGS) matmul.cpp -o cpp_matmul

clean:
	rm -f test_async_engine cpp_matmul cuda_matmul

.PHONY: clean