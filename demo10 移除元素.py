# 作者：宁方笑
# 开发时间：2021/3/21 21:30
def removeElement(nums,val):
    if len(nums)==0:
        return 0
    slow=0
    for quick in range(0,len(nums)):
        if nums[quick]!=val:
            nums[slow]=nums[quick]
            slow+=1
    return slow

nums=[0,1,2,2,3,0,4,2]
val=2
print(removeElement(nums,val))