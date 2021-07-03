# 作者：宁方笑
# 开发时间：2021/7/3 10:52
# 汉明距离是指两个数的二进制表示不同的位数
def hammingDistance(x, y):
    s = x ^ y  # 求x和y的异或，得到的结果中有几个1汉明距离就是多少
    count = 0
    while s:  # 通过与自减1的与运算，得到s中1的数目，即为答案
        s = s & s - 1
        count += 1
    return count


x = 1
y = 4
print(hammingDistance(x, y))
