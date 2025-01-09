#include <stdio.h>
#include <time.h>

int main() {
    const int size = 1000000;
    float array[size];

    // 初始化数组
    for(int i = 0; i < size; i++) {
        array[i] = (float)i;
    }

    float sum = 0.0f;
    clock_t start = clock();

    // 计算数组的和
    for(int i = 0; i < size; i++) {
        sum += array[i];
    }

    clock_t end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Total sum: %f\n", sum);
    printf("Time taken: %f seconds\n", time_taken);

    return 0;
}
