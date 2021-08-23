# 作者：宁方笑
# 开发时间：2021/8/23 21:17
def canJump(nums):
    n, rightmost = len(nums), 0
    for i in range(n):
        if i <= rightmost:
            rightmost = max(rightmost, i + nums[i])
            if rightmost >= n - 1:
                return True
    return False


nums =[3,2,1,0,4]
print(canJump(nums))