# 作者：宁方笑
# 开发时间：2021/9/12 18:18
def subsetsWithDup(nums):
    nums.sort()
    temp = []
    res = []
    def dfs(choosePre, cur):
        nonlocal temp
        if cur == len(nums):
            res.append(temp[:]) #注意，这里append方法需要temp的分割，不能直接传temp
            return
        dfs(False, cur + 1)
        if not choosePre and cur > 0 and nums[cur - 1] == nums[cur]:
            return
        temp.append(nums[cur])
        dfs(True, cur + 1)
        temp = temp[:len(temp) - 1]

    dfs(False, 0)
    return res


nums = [1,2,2]
print(subsetsWithDup(nums))