# 作者：宁方笑
# 开发时间：2021/4/9 16:24
def lengthOfLastWord(s:str):
    lst=s.split()
    if not lst:
        return 0
    return len(lst[-1])

s=" "
print(lengthOfLastWord(s))
