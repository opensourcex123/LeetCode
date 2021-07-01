# 作者：宁方笑
# 开发时间：2021/7/1 10:40
def minMoves(nums):
    return sum(nums) - len(nums) * min(nums) if len(nums) != 1 else 0   #数学解法

nums=[1,2,3]
print(minMoves(nums))