# 作者：宁方笑
# 开发时间：2021/3/6 20:00
def reverse(x):
    if x<0:
        x=abs(x)
        n=len(str(x))
        num=0
        for i in range(n):
            add=x%10
            num=num+add*(10**(n-1-i))
            x=x//10
        if num > (2 ** 31) - 1 or num < -(2 ** 31):
            print(0)
        else:
            print(-num)
    else:
        n = len(str(x))
        num = 0
        for i in range(n):
            add = x % 10
            num = num + add * (10 ** (n - 1 - i))
            x = x // 10
        if num > (2 ** 31) - 1 or num < -(2 ** 31):
            print(0)
        else:
            print(num)

x=-123
reverse(x)