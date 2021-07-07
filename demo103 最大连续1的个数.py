# 作者：宁方笑
# 开发时间：2021/7/7 10:44
def findMaxConsecutiveOnes(nums):
    res=[]
    count=0
    for i in nums:
        if i==1:
            count+=1
        elif i==0:
            res.append(count)
            count=0
        res.append(count)
    return max(res)

nums=[1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))