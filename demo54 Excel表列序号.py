# 作者：宁方笑
# 开发时间：2021/5/20 18:16
def titleToNumber(columnTitle):
    res=0
    j=1
    for i in range(len(columnTitle)-1,-1,-1):
        res=(ord(columnTitle[i])-64)*j+res
        j*=26
    return res

title='A'
print(titleToNumber(title))