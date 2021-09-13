# 作者：宁方笑
# 开发时间：2021/9/13 21:22
def numDecodings(s):
    n = len(s)
    f = [1] + [0] * n
    for i in range(1, n + 1):
        if s[i - 1] != '0':
            f[i] += f[i - 1]
        if i > 1 and s[i - 2] != '0' and int(s[i - 2: i]) <= 26:
            f[i] += f[i - 2]
    return f[n]


s = "12"
print(numDecodings(s))