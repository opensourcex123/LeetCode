# 作者：宁方笑
# 开发时间：2021/7/17 21:13
def detectCapitalUse(word):
    def isBigger(ch):
        return ch >= 'A' and ch <= 'Z'

    biggerstart = isBigger(word[0])
    n = len(word)
    cntbigger = 0
    if biggerstart:
        cntbigger += 1
        for i in range(1, n):
            if isBigger(word[i]):
                cntbigger += 1
    else:
        for i in range(1, n):
            if isBigger(word[i]):
                cntbigger += 1
    #三种情况，分类讨论
    return (biggerstart and cntbigger == n) or (biggerstart and cntbigger == 1) or (not biggerstart and cntbigger == 0)


word = "ffffffffffffffffffffF"
print(detectCapitalUse(word))
