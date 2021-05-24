# 作者：宁方笑
# 开发时间：2021/3/2 20:20
def addTwoNumbers(l1, l2):
    l3 = []
    n1 = len(l1)
    n2 = len(l2)
    add1 = 0
    add2 = 0
    for i in range(n1):
        add1 = add1 + l1[i] * (10 ** i)
    for j in range(n2):
        add2 = add2 + l2[j] * (10 ** j)
    add = add1 + add2
    if add==0:
        l3.append(0)
    while add != 0:
        num = add % 10
        l3.append(num)
        add = add // 10
    print(l3)

l1=[9,9,9,9,9,9,9]
l2=[9,9,9,9]
addTwoNumbers(l1,l2)