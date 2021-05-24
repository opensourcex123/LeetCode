# 作者：宁方笑
# 开发时间：2021/4/14 21:16
def moveZeroes(nums):
    i=0
    j=0
    while(j!=len(nums) and i!=len(nums)):   #快慢指针法，j为快指针，i为慢指针
        if nums[i]==0:
            j+=1
            if j==len(nums):    #防止数组越界
                break
            nums[i],nums[j]=nums[j],nums[i]
        else:
            i+=1
            if(i>j):    #如果慢指针比快指针还快，则将快指针调整一下
                j=i
    return nums

nums=[4,2,4,0,0,3,0,5,1,0]
print(moveZeroes(nums))
