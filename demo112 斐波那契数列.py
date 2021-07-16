# 作者：宁方笑
# 开发时间：2021/7/16 20:16
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=2
print(fib(n))