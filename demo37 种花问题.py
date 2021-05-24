# 作者：宁方笑
# 开发时间：2021/5/1 21:43
def canPlaceFlowers(flowerbed, n):  #强行种花
    count=0
    flowerbed=[0]+flowerbed+[0] #这样扩展数组，避免越界
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
            flowerbed[i]=1
            count+=1
    if count>=n:
        return True
    else:
        return False

flowerbed = [1,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed,n))