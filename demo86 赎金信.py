# 作者：宁方笑
# 开发时间：2021/6/20 11:10
def canConstruct(ransomNote, magazine):
    count={}
    for i in ransomNote:
        count[i]=ransomNote.count(i)
    for i in magazine:
        if i in count:
            count[i]-=1
    for key in count.keys():
        if count[key]>0:
            return False
    return True

ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote,magazine))