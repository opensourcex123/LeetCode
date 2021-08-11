# 作者：宁方笑
# 开发时间：2021/8/11 19:45
def searchRange(nums, target):
    # 寻找第一个等于target的下标和第一个大于target的下标-1
    def binarySearch(nums, target, lower):
        l, r = 0, len(nums) - 1
        res = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res

    leftIdx = binarySearch(nums, target, True)
    rightIdx = binarySearch(nums, target, False) - 1
    if leftIdx <= rightIdx and rightIdx <= len(nums) and nums[leftIdx] == target and nums[rightIdx] == target:
        return [leftIdx, rightIdx]
    else:
        return [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))
