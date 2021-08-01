# 作者：宁方笑
# 开发时间：2021/8/1 21:06
def threeSum(nums):
    n = len(nums)
    nums.sort()
    res = []

    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        third = n - 1
        target = -nums[first]
        for second in range(first + 1, n):  # 二重循环与三重循环合在了一起，减少了时间复杂度
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second == third:
                break
            if nums[second] + nums[third] == target:
                res.append([nums[first], nums[second], nums[third]])
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
