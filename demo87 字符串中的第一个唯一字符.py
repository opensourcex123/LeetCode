# 作者：宁方笑
# 开发时间：2021/6/21 11:14
import collections


def firstUniqChar(s):
    # count={}
    # for i in s:
    #     count[i]=s.count(i)
    frequency=collections.Counter(s)    #将s中的每一个字符进行计数
    for i,ch in enumerate(s):   #将s变成一个字典,索引在前，字符在后
        if frequency[ch]==1:
            return i
    return -1

s = "leetcode"
print(firstUniqChar(s))