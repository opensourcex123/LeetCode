# 作者：宁方笑
# 开发时间：2021/8/10 20:00
def search(nums, target):
    # if target not in nums:
    #     return -1
    # return nums.index(target)
    #有序数组查找就想二分查找
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target))