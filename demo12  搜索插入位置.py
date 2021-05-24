# 作者：宁方笑
# 开发时间：2021/4/6 21:28
def midSearch(nums,target): #二分法实现
    if target<nums[0]:
        return 0
    if target>nums[-1]:
        return len(nums)
    left=0
    right=len(nums)-1
    ans=len(nums)
    while left<=right:
        mid=(left+right)//2
        if nums[mid]>=target:   #如果目标数不存在数组中，还要返回该数在数组中的位置
            ans=mid
            right=mid-1
        else:
            left=mid+1
    return ans
nums=[1,2,4,5]
target=2
print(midSearch(nums,target))