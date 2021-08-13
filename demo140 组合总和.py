# 作者：宁方笑
# 开发时间：2021/8/13 21:07
def combinationSum(candidates, target):
    ans = []
    combine = []
    def dfs(res, idx):
        if idx >= len(candidates) or res >= target:
            if res == target:
                ans.append(combine[:])
            return
        combine.append(candidates[idx])
        dfs(res + candidates[idx], idx)
        combine.pop()
        dfs(res, idx + 1)
    dfs(0, 0)
    return ans


candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))