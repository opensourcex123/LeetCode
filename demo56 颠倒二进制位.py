# 作者：宁方笑
# 开发时间：2021/5/21 17:11
def reverseBits(n):
    res = 0
    for i in range(32):
        res = (res << 1) | (n & 1)  #按位与只留下第一位，res左移一位去按位或，取第一位
        n >>= 1 #n右移一位
    return res