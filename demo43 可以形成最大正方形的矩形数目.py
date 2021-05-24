# 作者：宁方笑
# 开发时间：2021/5/7 18:35
def countGoodRectangles(rectangles):
    maxlen=list()
    for i in rectangles:
        j=0
        if i[j]>=i[j+1]:
            maxlen.append(i[j+1])
        else:
            maxlen.append(i[j])
    maxlen.sort()
    count=0
    for i in range(0,-len(maxlen),-1):
        if maxlen[i]==maxlen[len(maxlen)-1]:
            count+=1
    return count

rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(countGoodRectangles(rectangles))