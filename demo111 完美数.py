# 作者：宁方笑
# 开发时间：2021/7/15 21:32
import math


def checkPerfectNumber(num):  # 欧几里得算法，计算完美数，目前发现的完美数都是偶数
    if num == 1:
        return False
    sum = 1
    for i in range(2, int(math.ceil(math.sqrt(num)))):
        if num % i == 0:
            sum += i
            if i * i != num:
                sum += num // i
    return sum == num


num = 8128
print(checkPerfectNumber(num))
