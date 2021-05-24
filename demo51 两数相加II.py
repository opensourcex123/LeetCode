# 作者：宁方笑
# 开发时间：2021/5/17 10:16
def twoSum(numbers, target):
    slow=0
    quick=len(numbers)-1
    while slow<quick:
        if numbers[slow]+numbers[quick]==target:
            return [slow+1,quick+1]
        elif numbers[slow]+numbers[quick]<target:
            slow+=1
        else:
            quick-=1
    return [-1,-1]

numbers = [2,3,4]
target = 6
print(twoSum(numbers,target))