# 作者：宁方笑
# 开发时间：2021/5/19 18:18
# coding=utf-8
def convertToTitle(columnNumber):
    s=''
    while columnNumber:
        columnNumber-=1
        s=chr((columnNumber%26)+65)+s   #chr数字变化字母，ord字母转数字
        columnNumber//=26
    return s

number=701
print(convertToTitle(number))