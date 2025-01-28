#include <iostream>
#include <cuda_runtime.h>
#include <chrono>

#define BLOCK_SIZE 16

// void printMatrix(const float* matrix, int N, const char* name){
//     const int print_size = 2048;
//     for (int i = 0; i < print_size && i < N; i++){
//         for (int j = 0; j < print_size && j < N; j++){
//             printf("%6.2f ", matrix[i * N + j]);
//         }
//         printf("\n");
//     }
//     printf("\n");
// }

__global__ void matrixMul(float *C, const float* A, const float* B, int N){
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    C[row * N + col] = 0.0f;
    // 就爱写点 python.
    if (row < N && col < N)
        for (size_t i = 0; i < N; i++) 
            C[row * N + col] += A[row * N + i] * B[i * N + col];
}

int main(int argc, char **argv){

    // TODO:
    // 1. 用户自定义矩阵大小
    // 2. bind 到 python api

    int N = 4096 * 8;
    size_t size = N * N * sizeof(float);

    // 分配 host 内存
    float* h_A = (float*) malloc(size);
    float* h_B = (float*) malloc(size);
    float* h_C = (float*) malloc(size);

    // init a random matrix
    for (int i = 0; i < N * N; ++i){
        h_A[i] = static_cast<float>(rand()) / RAND_MAX;
        h_B[i] = static_cast<float>(rand()) / RAND_MAX;
    }

    // 分配 deivce 内存
    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, size);
    cudaMalloc(&d_B, size);
    cudaMalloc(&d_C, size);

    // host -> device
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

    // caclulate
    dim3 dimBlock(BLOCK_SIZE, BLOCK_SIZE);
    dim3 dimGrid((N + dimBlock.x - 1)/dimBlock.x, (N + dimBlock.y -1)/dimBlock.y);
    auto start_time = std::chrono::high_resolution_clock::now();

    matrixMul<<<dimGrid, dimBlock>>>(d_C, d_A, d_B, N);

    cudaDeviceSynchronize();
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;
    printf("Time taken: %f seconds\n", elapsed.count());
    // 0.178791 seconds on 3090 for N = 4096
    // 1.359545 seconds on 3090 for N = 8192
    // 10.912323 seconds on 3090 for N = 16384
    // 88.934003 seconds on 3090 for N = 32768

    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

    // free device memory
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    // print & verify
    // first row of left matrix
    // for (size_t i = 0; i < N; i++) printf("%6.2f ", h_A[i]);
    // printf("\n");
    // first column of right matrix
    // for (size_t i = 0; i < N; i++) printf("%6.2f ", h_B[i * N]);
    // printf("\n");
    // first element of result
    std::cout << "result[0][0]: " << h_C[0] << std::endl;

    // free host memory
    free(h_A);
    free(h_B);
    free(h_C);

    return 0;
}