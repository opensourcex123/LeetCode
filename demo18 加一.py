# 作者：宁方笑
# 开发时间：2021/4/12 20:58
def plusOne(digits):
    s="".join(str(s) for s in digits)   #将列表替换成字符串
    num=int(s)+1    #将字符串转化成整数后+1
    num=str(num)    #再将运算结束的整数替换为字符串
    lst=[int(i) for i in num]   #将字符串转化为int在转化为列表
    return lst
num=[9,9]
print(plusOne(num))