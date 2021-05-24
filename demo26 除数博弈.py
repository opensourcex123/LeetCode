# 作者：宁方笑
# 开发时间：2021/4/20 21:28
def divisonGame(n):
    dp=[0 for i in range(n+1)]
    dp[1]=0
    if n<=1:
        return False
    else:
        dp[2]=1
        for i in range(3,n+1):
            for j in range(1,i):
                if i%j==0 and dp[i-j]==0:
                    dp[i]=1
                    break
        if dp[n]==1:
            return True
        else:
            return False

n=2
print(divisonGame(n))