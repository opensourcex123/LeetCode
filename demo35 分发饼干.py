# 作者：宁方笑
# 开发时间：2021/4/29 21:29
def findContentChirdren(g,s):
    g.sort()
    s.sort()
    m=len(s)
    n=len(g)
    i=j=count=0
    while i<n and j<m:
        while j<m and g[i]>s[j]:
            j+=1
        if j<m:
            count+=1
        i+=1
        j+=1
    return count

g = [1,2,3]
s = [1,1]
print(findContentChirdren(g,s))
