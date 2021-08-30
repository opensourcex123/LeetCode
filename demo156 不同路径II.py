# 作者：宁方笑
# 开发时间：2021/8/30 18:40
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    f = [0] * n
    if obstacleGrid[0][0] == 0:
        f[0] = 1
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                f[j] = 0
                continue
            if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
                f[j] += f[j - 1]
    return f[len(f) - 1]


obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))