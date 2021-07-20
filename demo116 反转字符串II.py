# 作者：宁方笑
# 开发时间：2021/7/20 21:33
def reverseStr(s,k):
    a=list(s)
    for i in range(0,len(a),2*k):
        a[i:i+k]=reversed(a[i:i+k])
    return "".join(a)

s='abcdefg'
k=2
print(reverseStr(s,k))