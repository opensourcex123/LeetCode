# 作者：宁方笑
# 开发时间：2021/7/22 20:51
def checkRecord(s):
    if s.count('A')>=2:
        return False
    for i in range(len(s)):
        if i+1<=len(s)-1 and i+2<=len(s)-1:
            if s[i]=='L' and s[i+1]=='L' and s[i+2]=='L' and i+2<=len(s)-1:
                return False
    return True

s="ALL"
print(checkRecord(s))