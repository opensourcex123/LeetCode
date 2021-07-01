# 作者：宁方笑
# 开发时间：2021/7/1 10:30
def findDisappearNumbers(nums):
    res=[]
    n=len(nums)
    hash=set(nums)
    for i in range(1,n+1):
        if i not in hash:
            res.append(i)
    return res

nums=[1,1]
print(findDisappearNumbers(nums))