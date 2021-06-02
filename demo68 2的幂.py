# 作者：宁方笑
# 开发时间：2021/6/2 9:50
def isPowerOfTwo(n):    #位运算，利用n&n-1可以直接将二进制n中的1去掉，如果剩下的均为0，则说明n是2的幂
    return n>0 and (n&(n-1))==0

n=511
print(isPowerOfTwo(n))