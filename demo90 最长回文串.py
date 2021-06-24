# 作者：宁方笑
# 开发时间：2021/6/24 10:52
import collections

def longestPalindrome(s: str) -> int:
    res=0
    fre=collections.Counter(s)
    for i in fre.values():
        res+=i//2*2 #大于1用偶数个，放在对称轴的一侧
        if res%2==0 and i%2==1: #如果结果是偶数，并且有的字母出现了奇数次，则可以用它做对称轴，但只能用一个
            res+=1
    return res

s="abccccdd"
print(longestPalindrome(s))