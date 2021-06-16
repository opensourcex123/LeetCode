# 作者：宁方笑
# 开发时间：2021/6/16 20:06
def reverseVowels(s):
    left=0
    right=len(s)-1
    list=[]
    for i in s:
        list.append(i)
    vowels=['a','e','i','o','u','A','E','I','O','U']
    while left<right:
        while list[left] not in vowels and left<right:
            left+=1
        while list[right] not in vowels and left<right:
            right-=1
        list[left],list[right]=list[right],list[left]
        left+=1
        right-=1
    s=''.join(list)
    return s

s='leetcode'
print(reverseVowels(s))