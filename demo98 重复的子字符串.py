# 作者：宁方笑
# 开发时间：2021/7/2 10:49
import collections

def repeatedSubstringPattern(str):
    freq=collections.Counter(str)
    # freq={i:str.count(i) for i in str}
    freq_list=list(freq.values())
    freq_hash=set(freq_list)
    if len(freq_hash)>1 or 1 in freq_hash:
        # print(freq_hash)
        return False
    else:
        # print(freq_hash)
        return True

s="abab"
print(repeatedSubstringPattern(s))