# 作者：宁方笑
# 开发时间：2021/6/1 10:12
def summaryRanges(nums):
    res=[]
    start=0
    final=0
    i=0
    while i<len(nums):  #判断数组是否越界
        if i+1<len(nums) and nums[i]==nums[i+1]-1:
            start=nums[i]
            while i+1<len(nums) and  nums[i]==nums[i+1]-1:
                final=nums[i+1]
                i+=1
            res.append(f"{start}->{final}")
            i+=1
        else:
            res.append(str(nums[i]))
            i+=1
    return res

nums= [0,1,2,4,5,7]
print(summaryRanges(nums))