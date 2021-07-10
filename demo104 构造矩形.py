# 作者：宁方笑
# 开发时间：2021/7/8 13:43
import math


def constructRectangle(area):
    w = int(math.sqrt(area))  # 宽度一定小于等于面积的开平方，因为长度必须大于等于宽度
    while area % w != 0:  # 找到第一个可以整除的便是答案
        w -= 1
    return [area // w, w]


area = 17
print(constructRectangle(area))
