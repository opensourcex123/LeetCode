# 作者：宁方笑
# 开发时间：2021/4/16 9:17
def mySqrt(x):
    i=1
    while i*i<=x:
        if i*i==x:
            return i
        i+=1
    return i-1


x=8
print(mySqrt(x))