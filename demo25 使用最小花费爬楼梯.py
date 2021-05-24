# 作者：宁方笑
# 开发时间：2021/4/19 20:44
def minCostClimbStaris(cost):
    n=len(cost)
    dp=[0]*(n+1)
    for i in range(2,n+1):
        dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    return dp[n]

cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbStaris(cost))