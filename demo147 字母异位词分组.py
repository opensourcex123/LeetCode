# 作者：宁方笑
# 开发时间：2021/8/20 19:17
import collections

def groupAnagrams(strs):
    mp = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))   # 将每一个字符串排序后做键
        mp[key].append(st)  # 将对应的字符串值添加到键中

    return list(mp.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))