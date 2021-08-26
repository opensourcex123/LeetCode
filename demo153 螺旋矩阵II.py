# 作者：宁方笑
# 开发时间：2021/8/26 20:59
def generateMatrix(n):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    matrix = [[0] * n for _ in range(n)]
    row, col, dir = 0, 0, 0
    for i in range(n * n):
        matrix[row][col] = i + 1
        dx, dy = dirs[dir]
        r, c = row + dx, col + dy
        if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
            dir = (dir + 1) % 4
            dx, dy = dirs[dir]
        row, col = row + dx, col + dy
    return matrix


nums = 3
print(generateMatrix(nums))