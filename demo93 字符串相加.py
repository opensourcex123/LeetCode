# 作者：宁方笑
# 开发时间：2021/6/27 10:58
def addStrings( num1 ,num2):
    res=''
    i,j,carry=len(num1)-1,len(num2)-1,0
    while i>=0 or j>=0:
        n1=int(num1[i]) if i>=0 else 0  #如果不对齐，则用置0处理
        n2=int(num2[j]) if j>=0 else 0
        tmp=n1+n2+carry
        carry=tmp//10
        res=str(tmp%10)+res #字符串拼接
        i-=1
        j-=1
    return '1'+res if carry!=0 else res #判断最后是否进位

num1='11'
num2='123'
print(addStrings(num1,num2))