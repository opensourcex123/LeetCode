# 作者：宁方笑
# 开发时间：2021/5/19 21:02
import collections
def majorityElement(nums):
    counts = collections.Counter(nums)  #collections模块，计数器，返回字典，键为列表值，值为出现的个数
    return max(counts.keys(),key=counts.get)    #key设置排序的对象

nums=[3,3,4]
print(majorityElement(nums))
# counts = collections.Counter([1,3,2,2,3,1,2])
# print(counts.get)