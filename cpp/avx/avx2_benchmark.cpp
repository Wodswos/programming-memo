/******************************************************
 * 编译 & 运行：
 * 
 ******************************************************/

#include <immintrin.h>
#include <stdio.h>
#include <time.h>

int main() {
    const int size = 1000000;
    float array[size];

    // 初始化数组
    for(int i = 0; i < size; i++) {
        array[i] = (float)i;
    }

    __m256 sum = _mm256_setzero_ps();  // 用于存放和的变量，初始为 0
    clock_t start = clock();

    // 使用 AVX2 指令计算和
    for(int i = 0; i < size; i += 8) {
        __m256 data = _mm256_loadu_ps(&array[i]);
        sum = _mm256_add_ps(sum, data);
    }

    // 将 sum 中的 8 个 float 值相加，得到最终的和
    float result[8];
    _mm256_storeu_ps(result, sum);
    float totalSum = result[0] + result[1] + result[2] + result[3] + result[4] + result[5] + result[6] + result[7];

    clock_t end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Total sum: %f\n", totalSum);
    printf("Time taken: %f seconds\n", time_taken);

    return 0;
}
