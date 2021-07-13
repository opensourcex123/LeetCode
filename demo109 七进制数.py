# 作者：宁方笑
# 开发时间：2021/7/13 21:41
def convertBase7(num):
    if num==0:
        return str(0)
    is_negative=num<0
    res=[]
    num=abs(num)
    while num>0:
        num,remain=num//7,num%7
        res.append(str(remain))
    return '-'+''.join(res[::-1]) if is_negative else ''.join(res[::-1])

num=1234
print(convertBase7(num))