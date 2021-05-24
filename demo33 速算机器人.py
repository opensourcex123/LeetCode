# 作者：宁方笑
# 开发时间：2021/4/27 21:15
def calculate(s):
    x=1
    y=0
    for i in s:
        if i=="A":
            x=2*x+y
        else:
            y=2*y+x
    return x+y

s="AB"
print(calculate(s))