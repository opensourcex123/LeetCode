# 作者：宁方笑
# 开发时间：2021/5/2 21:51
def lemonadeChange(bills):
    five=0
    ten=0
    for i in range(len(bills)):
        if bills[i]==5:
            five+=1
        elif bills[i]==10:
            if five>=1:
                five-=1
                ten+=1
            else:
                return False
        else:
            if five>=1 and ten>=1:
                ten-=1
                five-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True
bills=[10,10]
print(lemonadeChange(bills))