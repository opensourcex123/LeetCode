# 作者：宁方笑
# 开发时间：2021/5/10 16:02
def getRow(rowIndex):
    res = [1]
    for i in range(1, rowIndex + 1):
        res.append(1)
        for j in range(i - 1, 0, -1):
            res[j] = res[j] + res[j - 1]
    return res

row=3
print(getRow(row))