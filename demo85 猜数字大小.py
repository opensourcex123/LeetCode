# 作者：宁方笑
# 开发时间：2021/6/19 10:55
def guess(n):
    pass
def guessNumber(n):
    left=1
    right=n
    mid=(left+right)//2
    while guess(mid)!=0:
        if guess(mid)==0:
            return mid
        elif guess(mid)==1:
            left=mid+1
            mid=(left+right)//2
        else:
            right=mid
            mid=(left+right)//2

