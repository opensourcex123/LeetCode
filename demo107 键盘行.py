# 作者：宁方笑
# 开发时间：2021/7/12 8:42
def findWords(words):
    def findRow(ch):
        key = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        if ch.lower() in key[0]:
            return 0
        elif ch.lower() in key[1]:
            return 1
        else:
            return 2

    res = []
    for str in words:
        row = findRow(str[0])
        i = 0
        for i in range(1, len(str)):
            if findRow(str[i]) == row:
                continue
            else:
                i -= 1  # 解决最后一个字符是别的行的问题
                break
        if i == len(str) - 1:
            res.append(str)
    return res


words = ["abdfs", "cccd", "a", "qwwewm"]
print(findWords(words))
