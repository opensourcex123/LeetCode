# 作者：宁方笑
# 开发时间：2021/9/4 19:45
def combine(n, k):
    temp = []
    res = []
    def dfs(cur):
        nonlocal temp
        if len(temp) + (n - cur + 1) < k:
            return
        if len(temp) == k:
            res.append(temp)
            return
        temp.append(cur)
        dfs(cur + 1)
        temp = temp[:len(temp) - 1]
        dfs(cur + 1)
    dfs(1)
    return res


n = 4
k = 2
print(combine(n, k))