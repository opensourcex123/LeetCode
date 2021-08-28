# 作者：宁方笑
# 开发时间：2021/8/28 20:57
def uniquePaths(m, n):  # 动态规划
    f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
    print(f)

    for i in range(1, m):
        for j in range(1, n):
            f[i][j] = f[i - 1][j] + f[i][j - 1]

    return f[m - 1][n - 1]


m = 3
n = 7
print(uniquePaths(m, n))
