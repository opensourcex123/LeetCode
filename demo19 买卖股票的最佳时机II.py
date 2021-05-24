# 作者：宁方笑
# 开发时间：2021/4/14 21:10
def maxProfit(prices):
    profit=0
    for i in range(1,len(prices)):  #要从1开始
        tmp=prices[i]-prices[i-1]   #连续上涨日，连续下降日和不降不涨日
        if tmp>0:   #上涨日的时候进行利润增加
            profit+=tmp
    return profit

nums=[7,1,5,3,6,4]
print(maxProfit(nums))