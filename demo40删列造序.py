# 作者：宁方笑
# 开发时间：2021/5/4 15:28
def minDeletionSize(strs):
    length=len(strs[0])
    count=0
    for j in range(length):
        for i in range(len(strs)-1):    #内外层循环分清
            if strs[i][j]>strs[i+1][j]:
                count+=1
                break
    if count>0:
        return count
    else:
        return 0


strs = ["zyx","wvu","tsr"]
# print(len(strs[0]))
# print(strs[0][0]>strs[0][0])
print(minDeletionSize(strs))