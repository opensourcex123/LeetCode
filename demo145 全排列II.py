# 作者：宁方笑
# 开发时间：2021/8/18 21:07
def permuteUnique(nums):
    n = len(nums)
    nums.sort()
    res = []
    visit = [False for _ in range(len(nums))]
    def backtrack(idx):
        nonlocal perm
        if idx == n:
            res.append(perm[:])
            return
        for i in range(n):
            if visit[i] or i > 0 and not visit[i - 1] and nums[i] == nums[i - 1]:   # 保证不重复
                continue
            perm.append(nums[i])
            visit[i] = True
            backtrack(idx + 1)
            visit[i] = False
            perm = perm[:len(perm) - 1]


    perm = []
    backtrack(0)
    return res


nums = [1, 1, 2]
print(permuteUnique(nums))