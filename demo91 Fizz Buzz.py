# 作者：宁方笑
# 开发时间：2021/6/26 9:51
def fizzBuzz(n):
    res=[]
    for i in range(1,n+1):
        if i%3==0 and i%15!=0:
            res.append("Fizz")
        elif i%5==0 and i%15!=0:
            res.append("Buzz")
        elif i%15==0:
            res.append("FizzBuzz")
        else:
            res.append(f'{i}')
    return res

n=15
print(fizzBuzz(n))