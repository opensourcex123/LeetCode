# 作者：宁方笑
# 开发时间：2021/9/5 19:45
def subsets(nums):
    res = []
    s = []
    def dfs(cur):
        nonlocal s
        if cur == len(nums):
            res.append(s)
            return
        s.append(nums[cur])
        dfs(cur + 1)
        s = s[:len(s) - 1]
        dfs(cur + 1)
    dfs(0)
    return res


nums = [1,2,3]
print(subsets(nums))