# 作者：宁方笑
# 开发时间：2021/5/6 21:27
def balancedStringSplit(s):
    sumR=0
    sumL=0
    count=0
    for i in s:
        if i=='R':
            sumR+=1
        elif i=='L':
            sumL+=1
        if sumR==sumL:
            count+=1
            sumR=0
            sumL=0
    return count

s = "RLRRRLLRLL"
print(balancedStringSplit(s))