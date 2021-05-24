# 作者：宁方笑
# 开发时间：2021/3/9 19:22
def isValid(s:str)->bool:
    if len(s)%2!=0:
        print(False)
    pairs={")":"(","]":"[","}":"{"}
    stack=list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1]!=pairs[ch]:
                print(False)
            stack.pop()
        else:
            stack.append(ch)
    print(not stack)

s="([])"
isValid(s)