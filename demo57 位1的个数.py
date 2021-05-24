# 作者：宁方笑
# 开发时间：2021/5/22 22:09
def hammingWeight(n):
    count=0
    while n:
        n&=n-1  #这种运算是将n的最后一位1转为0，进行几次这种操作就说明有几个1
        count+=1
    return count