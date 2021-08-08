# 作者：宁方笑
# 开发时间：2021/8/8 21:02

def divide(dividend, divisor):
    sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
    a = abs(dividend)
    b = abs(divisor)

    time_bit_cnt = 0
    while a >= b:
        time_bit_cnt += 1
        b <<= 1
    time = 0
    while time_bit_cnt > 0:
        time_bit_cnt -= 1
        b >>= 1
        if a >= b:
            time += (1 << time_bit_cnt)
            a -= b
    time *= sign
    return time if -(1 << 31) <= time <= (1 << 31) - 1 else (1 << 31)-1


dividend = -2147483648
divisor = -1
print(divide(dividend, divisor))
