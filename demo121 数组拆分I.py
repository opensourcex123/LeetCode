# 作者：宁方笑
# 开发时间：2021/7/26 18:41
def arrayPairSum(nums):
    nums.sort()
    return sum(nums[::2])

nums=[1,4,3,2]
print(arrayPairSum(nums))