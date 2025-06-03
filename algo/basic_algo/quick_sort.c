#include <stdio.h>
#include <stdlib.h> // 用于 qsort（如果你想对比）和 rand（如果你想生成随机测试数据）

// 辅助函数：打印数组
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// --- 你需要实现这个函数 ---
/**
 * @brief 对整数数组的指定范围进行快速排序
 *
 * @param arr 要排序的数组
 * @param low 排序范围的起始索引 (包含)
 * @param high 排序范围的结束索引 (包含)
 */
void quickSort(int arr[], int low, int high){
    // printf("call quick sort with low %d, high %d \n", low, high);
    if (high - low <= 0)  return;
    int pivot_index = low, left_index = low + 1, right_index = high;

    while(left_index <= right_index){
        if (arr[left_index] < arr[pivot_index]){
            int tmp = arr[pivot_index];
            arr[pivot_index] = arr[left_index];
            arr[left_index] = tmp;
            pivot_index = left_index;
            left_index += 1;
        }
        // arr[left_index] < arr[pivot_index] && arr[right_index] < arr[pivot_index]
        else if (arr[right_index] < arr[pivot_index]){
            // 三者互换
            int tmp = arr[pivot_index];
            arr[pivot_index] = arr[right_index];
            arr[right_index] = arr[left_index];
            arr[left_index] = tmp;
            pivot_index = left_index;
            left_index += 1;
            right_index -= 1;
        }
        else{
            right_index -= 1;
        }
        // printArray(arr, high - low + 1);
        // printf("pivot index %d \n", pivot_index);
    }
    quickSort(arr, low, pivot_index - 1);
    quickSort(arr, pivot_index + 1, high);

}


// 主函数，用于测试
int main() {
    // 测试用例 1: 基本情况
    int arr1[] = {10, 7, 8, 9, 1, 5};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    printf("原始数组 1: ");
    printArray(arr1, n1);
    quickSort(arr1, 0, n1 - 1);
    printf("排序后数组 1: ");
    printArray(arr1, n1);
    printf("预期结果 1: 1 5 7 8 9 10\n\n");

    // 测试用例 2: 已排序数组
    int arr2[] = {1, 2, 3, 4, 5};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    printf("原始数组 2: ");
    printArray(arr2, n2);
    quickSort(arr2, 0, n2 - 1);
    printf("排序后数组 2: ");
    printArray(arr2, n2);
    printf("预期结果 2: 1 2 3 4 5\n\n");

    // 测试用例 3: 逆序数组
    int arr3[] = {5, 4, 3, 2, 1};
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    printf("原始数组 3: ");
    printArray(arr3, n3);
    quickSort(arr3, 0, n3 - 1);
    printf("排序后数组 3: ");
    printArray(arr3, n3);
    printf("预期结果 3: 1 2 3 4 5\n\n");

    // 测试用例 4: 包含重复元素的数组
    int arr4[] = {4, 1, 3, 4, 1, 2, 4, 2};
    int n4 = sizeof(arr4) / sizeof(arr4[0]);
    printf("原始数组 4: ");
    printArray(arr4, n4);
    quickSort(arr4, 0, n4 - 1);
    printf("排序后数组 4: ");
    printArray(arr4, n4);
    printf("预期结果 4: 1 1 2 2 3 4 4 4\n\n");

    // 测试用例 5: 包含负数的数组
    int arr5[] = {-3, 10, -7, 0, 5, -1};
    int n5 = sizeof(arr5) / sizeof(arr5[0]);
    printf("原始数组 5: ");
    printArray(arr5, n5);
    quickSort(arr5, 0, n5 - 1);
    printf("排序后数组 5: ");
    printArray(arr5, n5);
    printf("预期结果 5: -7 -3 -1 0 5 10\n\n");

    // 测试用例 6: 单个元素的数组
    int arr6[] = {42};
    int n6 = sizeof(arr6) / sizeof(arr6[0]);
    printf("原始数组 6: ");
    printArray(arr6, n6);
    quickSort(arr6, 0, n6 - 1);
    printf("排序后数组 6: ");
    printArray(arr6, n6);
    printf("预期结果 6: 42\n\n");

    // 测试用例 7: 空数组 (或者说，low > high 的情况，你的 quickSort 需要能正确处理)
    int arr7[] = {}; // 或者你可以传一个非空数组但 low > high
    int n7 = sizeof(arr7) / sizeof(arr7[0]); // n7 会是 0
    printf("原始数组 7 (空): ");
    printArray(arr7, n7);
    if (n7 > 0) { // 仅当数组非空时调用，或者你的 quickSort 能处理 n-1 为负数的情况
        quickSort(arr7, 0, n7 - 1);
    } else { // 对于空数组，我们手动处理或者确保 quickSort(arr, 0, -1) 不会导致错误
        printf(" quickSort(arr, 0, -1) 被跳过或应能安全处理 \n");
    }
    printf("排序后数组 7 (空): ");
    printArray(arr7, n7);
    printf("预期结果 7 (空): \n\n");

    return 0;
}