# 作者：宁方笑
# 开发时间：2021/9/18 16:29
def isInterLeave(s1, s2, s3):  # 动态规划
    m, n, t = len(s1), len(s2), len(s3)
    if m + n != t:
        return False

    f = [[False] * (n + 1) for _ in range(m + 1)]
    f[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            p = i + j - 1
            if i > 0:
                f[i][j] = f[i][j] or (f[i - 1][j] and s1[i - 1] == s3[p])
            if j > 0:
                f[i][j] = f[i][j] or (f[i][j - 1] and s2[j - 1] == s3[p])
    return f[m][n]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterLeave(s1, s2, s3))
