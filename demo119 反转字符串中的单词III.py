# 作者：宁方笑
# 开发时间：2021/7/24 20:46
def reverseWords(s):
    str1=s.split(' ')
    res=[]
    for str2 in str1:
        str2_list=list(str2)
        str2_list.reverse()
        str2=''.join(str2_list)
        res.append(str2)
    return ' '.join(res)

s="Let's take LeetCode contest"
print(reverseWords(s))