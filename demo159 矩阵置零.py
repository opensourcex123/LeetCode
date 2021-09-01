# 作者：宁方笑
# 开发时间：2021/9/1 21:09
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    row, col = [False] * m, [False] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = col[j] = True

    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))