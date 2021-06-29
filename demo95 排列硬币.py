# 作者：宁方笑
# 开发时间：2021/6/29 10:48
def arrangeCoins(n):
    for i in range(n+1):    #另外可以使用数学方法，k的最大值肯定比根号2n要小，所以我们的最大值可以设置为根号2n，然后不停缩小，找到第一个满足k * (k + 1) > 2 * n的k即可
        sn=((1+i)*i)//2
        if sn>n:
            return i-1
        elif sn==n:
            return i

n=8
print(arrangeCoins(n))