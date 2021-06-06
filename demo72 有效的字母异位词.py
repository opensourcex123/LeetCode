# 作者：宁方笑
# 开发时间：2021/6/6 11:12
def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    dic={}
    for i in range(len(s)): #将字母和频率构成哈希表存储起来
        if s[i] in dic:
            dic[s[i]]=dic[s[i]]+1
        else:
            dic[s[i]]=1
    for i in range(len(t)):
        if t[i] in dic:
            dic[t[i]]-=1
        else:
            return False
    for i in range(len(s)): #判断哈希表中的频率值是否小于0，小于0则判断错
        if dic[s[i]]<0:
            return False
    return True

s = "rat"
t = "car"
print(isAnagram(s,t))