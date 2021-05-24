# 作者：宁方笑
# 开发时间：2021/4/11 20:54
class Solution():
    def climbStaris(self,n):
        if n==0:
            return 1
        elif n==1:
            return 1
        else:
            return self.climbStaris(n-1)+self.climbStaris(n-2)

s=Solution()
print(s.climbStaris(5))