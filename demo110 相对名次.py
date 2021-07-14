# 作者：宁方笑
# 开发时间：2021/7/14 21:16
def findRelativeRanks(score):
    dic={i:score.index(i) for i in score}
    score.sort(reverse=True)
    dic[score[0]]='Gold Medal'
    dic[score[1]]='Silver Medal'
    dic[score[2]]='Bronze Medal'
    for i in range(3,len(score)):
        dic[score[i]]=str(i+1)
    return list(dic.values())

score=[1,2,3,4,5]
print(findRelativeRanks(score))