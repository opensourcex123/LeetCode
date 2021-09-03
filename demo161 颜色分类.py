# 作者：宁方笑
# 开发时间：2021/9/3 21:12
def sortColor(nums):    # 双指针
    n = len(nums)
    p0, p1 = 0, 0
    for i in range(n):
        if nums[i] == 1:
            nums[i], nums[p1] = nums[p1], nums[i]
            p1 +=1
        elif nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            if p0 < p1:
                nums[i], nums[p1] = nums[p1], nums[i]
            p0 += 1
            p1 += 1
    return nums


nums = [2,0,2,1,1,0]
print(sortColor(nums))