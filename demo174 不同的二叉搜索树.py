# 作者：宁方笑
# 开发时间：2021/9/16 20:55
def numTrees(n):    # 动态规划
    G = [0] * (n + 1)
    G[0], G[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            G[i] += G[j - 1] * G[ i - j]
    return G[n]

n = 3
print(numTrees(n))