MPICC = mpicxx
NVCC  = nvcc

test_nccl: test_nccl.cu
	$(NVCC) -o $@ $< -lnccl -lcudart -I$(MPI_INCLUDE) -L$(MPI_LIB) -lmpi


clean:
	rm -f test_nccl *.o