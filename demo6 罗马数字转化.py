# 作者：宁方笑
# 开发时间：2021/3/7 20:23
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
def compare(s1,s2):
    n1=d.get(s1)
    n2=d.get(s2)
    if n1<n2:
        return True
    else:
        return False
def romanToInt(self,s):
    n=len(s)
    num=0
    for i in range(n):
        if i<n-1 and compare(s[i],s[i+1]):
            num=num-d.get(s[i])
        else:
            num=num+d.get(s[i])
    print(num)

s="MCMXCIV"
romanToInt(s)