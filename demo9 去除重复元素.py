# 作者：宁方笑
# 开发时间：2021/3/11 20:46
def removeDuplicates(nums): #快慢指针解法
    j=0
    for i in range(len(nums)):
       if nums[i]!=nums[j]:
           j+=1
           nums[j]=nums[i]
    return j+1

num=[0,0,1,1,1,2,2,3,3,4,5,5,5]
print(removeDuplicates(num))