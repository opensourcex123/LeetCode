# 作者：宁方笑
# 开发时间：2021/5/25 9:58
def countPrimes(n): #埃拉托斯特尼筛法
    """
    求n以内的所有质数个数（纯python代码）
    """
    # 最小的质数是 2
    if n < 2:
        return 0

    isPrime = [1] * n
    isPrime[0] = isPrime[1] = 0  # 0和1不是质数，先排除掉

    # 埃式筛，把不大于根号 n 的所有质数的倍数剔除
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)   #n到i平方的距离除以跳跃的倍数即为0的个数

    return sum(isPrime)


n = 10
print(countPrimes(n))
