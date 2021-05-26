# 作者：宁方笑
# 开发时间：2021/5/26 9:24
def isIsomorphic(s, t): #维护两个字典，分别映射
    dic1={}
    dic2={}
    for i in range(len(s)):
        if s[i] in dic1 and dic1[s[i]]!=t[i] or t[i] in dic2 and dic2[t[i]]!=s[i]:
            return False
        dic1[s[i]]=t[i]
        dic2[t[i]]=s[i]
    return True

s='ega'
t='add'
print(isIsomorphic(s,t))