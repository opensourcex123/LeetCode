# 作者：宁方笑
# 开发时间：2021/6/15 21:17
def countBits(n):
    def countOnes(x):
        ones=0
        while x>0:
            x=x&(x-1)   #这种操作可以将x的最后一位1改为0，最多少这种操作，就有多少个1
            ones+=1
        return ones
    return [countOnes(i) for i in range(n+1)]

n=5
print(countBits(n))