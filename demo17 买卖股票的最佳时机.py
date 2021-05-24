# 作者：宁方笑
# 开发时间：2021/4/11 21:42
def maxProfit(prices):
    min=10000
    maxpro=0
    for x in prices:    #遍历一遍，要在最低点买入，最高点卖出
        if x<min:
            min=x
        elif maxpro<x-min:
            maxpro=x-min
    return maxpro
prices=[7,1,5,3,6,4]
print(maxProfit(prices))