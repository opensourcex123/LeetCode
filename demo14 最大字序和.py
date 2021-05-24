# 作者：宁方笑
# 开发时间：2021/4/9 9:38
def maxSubArray(nums):  #动态规划
    pre=0
    maxAns=nums[0]
    for x in nums:
        pre=max(pre+x,x)    #通过这个来改变起始元素
        maxAns=max(maxAns,pre)  #这个返回最大加和
    return maxAns

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))