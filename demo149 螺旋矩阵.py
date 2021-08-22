# 作者：宁方笑
# 开发时间：2021/8/22 21:16
def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, columns = len(matrix), len(matrix[0])
    visited = [[False] * columns for _ in range(rows)]
    total = rows * columns
    order = [0] * total

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    row, column = 0, 0
    directionIndex = 0
    for i in range(total):
        order[i] = matrix[row][column]
        visited[row][column] = True
        nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
        if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
            directionIndex = (directionIndex + 1) % 4
        row = row + directions[directionIndex][0]
        column = column + directions[directionIndex][1]
    return order


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))
