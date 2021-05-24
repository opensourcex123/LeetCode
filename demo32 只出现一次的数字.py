# 作者：宁方笑
# 开发时间：2021/4/26 21:55
from functools import reduce
def singleNumber(nums):
    return reduce(lambda x,y:x^y ,nums) #lamda匿名表达式，reduce函数

nums=[2,2,1]
print(singleNumber(nums))