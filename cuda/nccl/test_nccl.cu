/******************************************************
 * filename: test_nccl.cu
 * compile & run: make test_nccl && mpirun -np 2 ./test_nccl
 ******************************************************/

/*
TODO: 
 * Q: Reduce 操作是否可以用 send buffer 作为 recv buffer ?
 * A: Yes.
 * Q: C++ enumerate 可不可以用对应的值？
 * A: No, argument of type "int" is incompatible with parameter of type "cudaMemcpyKind"
*/


#include <mpi.h>
#include <nccl.h>
#include <cuda_runtime.h>
#include <iostream>
#include <vector>

#define CHECK_CUDA(call)                                                     \
    do{                                                                      \
        cudaError_t err = call;                                              \
        if(err != cudaSuccess){                                              \
            std::cerr << "CUDA error at " << __FILE__ << ":" << __LINE__     \
                      << " code=" << err << "\"" << cudaGetErrorString(err)  \
                      << "\"" << std::endl;                                   \
            exit(EXIT_FAILURE);                                               \
        }                                                                    \
    }while(0)

#define CHECK_NCCL(call) \
    do{ \
        ncclResult_t err = call; \
        if (err != ncclSuccess){ \
            std::cerr << "NCCL error at " << __FILE__ << ":" << __LINE__ \
                      << "code=" << err << "\"" << ncclGetErrorString(err) \
                      << "\"" << std::endl; \
            exit(EXIT_FAILURE); \
        } \
    }while(0)

int main(int argc, char* argv[]){
    // 1. init mpi
    MPI_Init(&argc, &argv);

    int world_size = 0;
    int world_rank = 0;

    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    
    // 2. init ncclComm
    // get and broadcast ncclUniqueId
    ncclUniqueId id;
    if(world_rank == 0) {
        CHECK_NCCL(ncclGetUniqueId(&id));
    }
    MPI_Bcast((void *) &id, sizeof(id), MPI_BYTE, 0, MPI_COMM_WORLD);

    int gpu_id = world_rank;
    CHECK_CUDA(cudaSetDevice(gpu_id));

    // ncclComm
    ncclComm_t comm;
    CHECK_NCCL(ncclCommInitRank(&comm, world_size, id, world_rank));

    // 3. prepare communication data/buffer
    const int data_size=8;
    std::vector<float> host_send(data_size, float(world_rank+1));
    std::vector<float> host_recv(data_size, 0.0f);

    float *device_send = nullptr;
    float *device_recv = nullptr;

    CHECK_CUDA(cudaMalloc(&device_send, data_size * sizeof(float)));
    CHECK_CUDA(cudaMalloc(&device_recv, data_size * sizeof(float)));

    CHECK_CUDA(cudaMemcpy(device_send, host_send.data(), data_size * sizeof(float), cudaMemcpyHostToDevice));
    CHECK_CUDA(cudaMemcpy(device_recv, host_recv.data(), data_size * sizeof(float), cudaMemcpyHostToDevice));

    // 4. Communication
    cudaStream_t stream;
    CHECK_CUDA(cudaStreamCreate(&stream));

    CHECK_NCCL(ncclAllReduce(
        (const void*)device_send,
        (void*) device_recv,
        // (void*) device_send,
        data_size,
        ncclFloat,
        ncclSum,
        comm,
        stream
    ));
    
    CHECK_CUDA(cudaStreamSynchronize(stream));

    // 5. Copy back to host and print
    CHECK_CUDA(cudaMemcpy(host_recv.data(), device_recv, data_size * sizeof(float), cudaMemcpyDeviceToHost));
    // CHECK_CUDA(cudaMemcpy(host_recv.data(), device_send, data_size * sizeof(float), cudaMemcpyDeviceToHost));

    std::cout << "[Rank " << world_rank << "] After AllReduce: ";
    for (int i = 0; i < data_size; i++){
        std::cout << host_recv[i] << " ";
    }
    std::cout << std::endl;
    
    // 6. Clear device
    CHECK_CUDA(cudaFree(device_send));
    CHECK_CUDA(cudaFree(device_recv));
    CHECK_CUDA(cudaStreamDestroy(stream));
    ncclCommDestroy(comm);

    MPI_Finalize();
    return 0;
}