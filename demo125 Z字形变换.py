# 作者：宁方笑
# 开发时间：2021/7/29 21:36
def convert(s,numRows):
    if numRows<2:
        return s
    res=["" for _ in range(numRows)]
    i,flag=0,-1
    for c in s:
        res[i]+=c
        if i==0 or i==numRows-1:    #转向
            flag=-flag
        i+=flag
    return "".join(res)

s = "PAYPALISHIRING"
numRows = 3
print(convert(s,numRows))