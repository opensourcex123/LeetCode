# 作者：宁方笑
# 开发时间：2021/6/10 10:11
def missingNumber(nums):
    n=len(nums)
    num_set=set(nums)   #哈希表的查找速度是O（1），要比列表要快
    for i in range(n+1):
        if i not in num_set:
            return i

nums =  [0]
print(missingNumber(nums))