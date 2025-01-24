import timeit


def matrix_multiply(A, B):
    # 获取矩阵 A 和 B 的维度
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # 检查矩阵 A 的列数是否等于矩阵 B 的行数
    if cols_A != rows_B:
        raise ValueError("矩阵 A 的列数必须等于矩阵 B 的行数")

    # 初始化结果矩阵 C，其维度为 (rows_A, cols_B)
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # 进行矩阵乘法
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # 或者是 rows_B
                C[i][j] += A[i][k] * B[k][j]

    return C


# 示例矩阵
A = [[i for i in range(1000)] for _ in range(1000)]
B = [[i for i in range(1000)] for _ in range(1000)]

# # 计算矩阵乘法
# for _ in range(1000):
#     result = matrix_multiply(A, B)

print(timeit.timeit(lambda: matrix_multiply(A, B), number=3))
# ~1097s/iter
