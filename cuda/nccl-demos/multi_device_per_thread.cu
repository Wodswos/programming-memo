/******************************************************
 * 文件名: multi_device_per_thread.cu
 * refer to https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/examples.html#example-3-multiple-devices-per-thread
 * 编译:  mpicxx -o mdpt multi_device_per_thread.cu -lnccl -lcudart -lcuda
 * 运行:  mpirun -np 2 ./mdpt  (可根据需要修改 -np)
 ******************************************************/


#include <stdio.h>
#include "cuda_runtime.h"
#include "nccl.h"
#include