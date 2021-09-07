# 作者：宁方笑
# 开发时间：2021/9/7 19:37
def removeDuplicates(nums): # 双指针
    n = len(nums)
    if n <= 2:
        return n
    slow, fast = 2, 2
    while fast < n:
        if nums[slow - 2] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))