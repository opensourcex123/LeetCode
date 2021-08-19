# 作者：宁方笑
# 开发时间：2021/8/19 21:03
def rotate(matrix):
    n = len(matrix)
    matrix_new =[[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix_new[j][n - i - 1] = matrix[i][j]

    matrix = matrix_new
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))