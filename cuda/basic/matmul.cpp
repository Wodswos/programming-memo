#include <iostream>
#include <vector>
#include <chrono>

void matrixMul(const std::vector<float>& leftMatrix, const std::vector<float>& rightMatrix, std::vector<float>& resMatrix, int N){
    for (int i = 0; i < N; ++i){
        for (int j = 0; j < N; ++j){
            float sum = 0.0f;
            for (int k = 0; k < N; ++k){
                sum += leftMatrix[i * N + k] * rightMatrix[k * N + j];
            }
            resMatrix[i* N + j] = sum;
        }
    }
}

int main(){
    int N = 4096;
    std::vector<float> A(N * N);
    std::vector<float> B(N * N);
    std::vector<float> C(N * N);

    for (int i = 0; i < N * N; i++){
        A[i] = static_cast<float>(rand()) / RAND_MAX;
        B[i] = static_cast<float>(rand()) / RAND_MAX;
    }

    auto start = std::chrono::high_resolution_clock::now();
    matrixMul(A, B, C, N);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Time taken: " << elapsed.count() << "seconds" << std::endl;

    // print & verify
    // first row of left matrix
    // for (size_t i = 0; i < N; i++) printf("%6.2f ", A[i]);
    // printf("\n");
    // first column of right matrix
    // for (size_t i = 0; i < N; i++) printf("%6.2f ", B[i * N]);
    // printf("\n");
    // first element of result
    std::cout << "result[0][0]: " << C[0] << std::endl;
    // 613 seconds for N = 4096

    return 0;
}