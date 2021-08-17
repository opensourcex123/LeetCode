# 作者：宁方笑
# 开发时间：2021/8/17 20:45
def permute(nums):
    def backtrack(first = 0):
        if first == len(nums):
            res.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] =nums[i], nums[first]


    res = []
    backtrack()
    return res

nums = [1, 2, 3]
print(permute(nums))