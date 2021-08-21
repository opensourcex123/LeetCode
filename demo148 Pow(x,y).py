# 作者：宁方笑
# 开发时间：2021/8/21 20:50

# 快速幂算法
def myPow(x, n):
    def quickMul(N):
        if N == 0:
            return 1.0
        y = quickMul(N // 2)
        return y * y if N % 2 == 0 else y * y * x

    res = quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
    return res


x = 2.00000
n = 10
print(myPow(x, n))