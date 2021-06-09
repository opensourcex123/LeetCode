# 作者：宁方笑
# 开发时间：2021/6/9 15:37
def isUgly(n):  #丑数是质因数只有2，3，5的数
    if n<=0:
        return False
    factors=[2,3,5]
    for factor in factors:  #所以思路为不断的除2,3,5这3个数，如果最后结果为1，则是丑数，反之
        while n%factor==0:
            n//=factor
    return n==1

n=6
print(isUgly(n))