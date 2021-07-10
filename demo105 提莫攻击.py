# 作者：宁方笑
# 开发时间：2021/7/10 21:28
def findPoisonedDuration(timeSeries, duration):
    res=0
    for i in range(0,len(timeSeries)-1):
        res+=min(timeSeries[i+1]-timeSeries[i],duration)
    return res+duration

timeSeries=[1,2]
duration=2
print(findPoisonedDuration(timeSeries,duration))