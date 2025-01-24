NVCC  = nvcc

CFLAGS = -O3 -std=c++11

# CUDA Architecture Version
ARCH = sm_80  # corresponding to RXT3080 / A100, don't use v100.

# target

test_async_engine: test_async_engine.cu
	$(NVCC) $(CFLAGS) -arch=$(ARCH)	-o $@ $<

matrix_multiply:
	:

clean:
	rm -f test_async_engine

.PHONY: clean