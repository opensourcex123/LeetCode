# 作者：宁方笑
# 开发时间：2021/9/11 21:05
def grayCode(n):
    res, head = [0], 1
    for i in range(n):
        for j in range(len(res) - 1, -1, -1):
            res.append(head + res[j])
        head <<= 1
    return res


n = 2
print(grayCode(n))