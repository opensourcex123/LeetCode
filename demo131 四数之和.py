# 作者：宁方笑
# 开发时间：2021/8/4 21:02
def fourSum(nums,target):
    res=list()
    if not nums and len(nums)<4:
        return res

    nums.sort()
    length=len(nums)
    for i in range(length-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        if nums[i] + nums[i+1] +nums[i+2] +nums[i+3] > target:
            break
        if nums[i]+ nums[length-3] +nums[length-2] +nums[length-1] <target:
            continue
        for j in range(i+1,length-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            if nums[i] + nums[j] +nums[j+1] + nums[j+2] >target:
                break
            if nums[i] + nums[j] +nums[length-2] +nums[length-1] < target:
                continue
            left, right = j+1 ,length-1
            while left < right:
                total=nums[i] +nums[j] + nums[left] +nums[right]
                if total==target:
                    res.append([nums[i],nums[j],nums[left],nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    right-=1
                elif total > target:
                    right-=1
                else:
                    left+=1
    return res


nums = [-2,-1,-1,1,1,2,2]
target = 0
print(fourSum(nums,target))