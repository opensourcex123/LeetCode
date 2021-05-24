# 作者：宁方笑
# 开发时间：2021/5/23 21:08
def isHappy(n): #要不进循环，要不等于1，要不无限增大，但无限增大会逐渐变为前2种情况
    def getNext(n):
        target=0
        while n>0:
            n,div=divmod(n,10)  #返回n//10，n%10
            target=div**2+target
        return target
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        n=getNext(n)
    return n==1

num=2
print(isHappy(num))