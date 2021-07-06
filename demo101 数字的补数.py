# 作者：宁方笑
# 开发时间：2021/7/6 9:07
def findComplement(num):
    rank=len(bin(num))-2    #确保位数相同
    return num^(2**rank-1)

num=5
print(findComplement(num))