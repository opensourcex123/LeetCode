# 作者：宁方笑
# 开发时间：2021/3/23 8:59
def strStr(haystack,needle):
    i=len(haystack)
    j=len(needle)
    if j==0:
        return 0
    for start  in range(i-j+1):
        if haystack[start:start+j]==needle:
            return start
    return -1
haystack="hello"
needle="ll"
print(strStr(haystack,needle))