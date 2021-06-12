# 作者：宁方笑
# 开发时间：2021/6/12 10:37
def wordPattern(pattern,s): #构造一个双射哈希表
    word2ch=dict()
    ch2word=dict()
    words=s.split(' ')
    if len(pattern)!=len(words):
        return False
    for ch,word in zip(pattern,words):
        if (ch in ch2word and ch2word[ch]!=word) or (word in word2ch and word2ch[word]!=ch):
            return False
        word2ch[word]=ch
        ch2word[ch]=word
    return True
pattern = "abba"
str = "dog dog dog dog"
print(wordPattern(pattern,str))