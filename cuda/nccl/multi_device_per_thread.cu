/******************************************************
 * filename: multi_device_per_thread.cu
 * From https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/examples.html#example-3-multiple-devices-per-thread
 * compile & run:  make stmp &&  mpirun -np 2 ./stmd 
 ******************************************************/


#include <stdio.h>
#include "cuda_runtime.h"
#include "nccl.h"
