# 作者：宁方笑
# 开发时间：2021/4/21 21:44
def yanghuiTriangle(numRows):
    ret=list()
    for i in range(numRows):
        row=list()
        for j in range(i+1):
            if j==0 or j==i:
                row.append(1)
            else:
                row.append(ret[i-1][j-1]+ret[i-1][j])
        ret.append(row)
    return ret

num=5
ret=yanghuiTriangle(num)
for i in range(len(ret)):
    print(ret[i],end="\n")