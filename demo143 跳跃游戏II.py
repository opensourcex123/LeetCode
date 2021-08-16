# 作者：宁方笑
# 开发时间：2021/8/16 19:35
def jump(nums):
    n = len(nums)
    maxPos, end, step = 0, 0, 0
    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
    return step


nums = [2, 3, 1, 1, 4]
print(jump(nums))