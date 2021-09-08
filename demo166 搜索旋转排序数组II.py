# 作者：宁方笑
# 开发时间：2021/9/8 21:27
def search(nums, target):
    n = len(nums)
    if not nums:
        return False
    if n == 1:
        return nums[0] == target
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        if nums[l] == nums[mid] and nums[mid] == nums[r]:
            l += 1
            r -= 1
        elif nums[l] <= nums[mid]:  # 左边界升序
            if nums[l] <= target < nums[mid]:
                r -= 1
            else:
                l += 1
        else:
            if nums[mid] < target <= nums[r]:
                l += 1
            else:
                r -= 1
    return False


nums = [2,5,6,0,0,1,2]
target = 0
print(search(nums, target))