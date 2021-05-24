# 作者：宁方笑
# 开发时间：2021/4/28 21:16
def isSubsequence(s,t):
    m=len(s)
    n=len(t)
    i=0
    j=0
    while i<m and j<n:
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==m

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))