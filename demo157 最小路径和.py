# 作者：宁方笑
# 开发时间：2021/8/30 19:13
def minPathSum(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))