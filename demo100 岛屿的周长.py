# 作者：宁方笑
# 开发时间：2021/7/4 10:46
def islandPerimeter(grid):
    res = 0
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                continue
            num = 4
            distances = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 判断上下左右是否有陆地相连，如果有，边长4减一，有几个减几个
            for distance in distances:
                newx, newy = i + distance[0], j + distance[1]
                if 0 <= newx < row and 0 <= newy < col and grid[newx][newy] == 1:  # 没有超出范围并且有相邻块
                    num -= 1
            res += num
    return res


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid))
