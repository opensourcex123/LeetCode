# 作者：宁方笑
# 开发时间：2021/6/8 18:48
def addDigits(num): #思路再与数学分析，是9的倍数最终相加为9，不是9的倍数最后是对9的余数
    if num==0:
        return 0
    if num%9==0:
        return 9
    return num%9

num=17
print(addDigits(num))