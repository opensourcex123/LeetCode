# 作者：宁方笑
# 开发时间：2021/8/25 20:59
def insert(intervals, newInterval):
    # intervals.append(newInterval)
    # intervals.sort(key=lambda x: x[0])
    #
    # merged = []
    # for interval in intervals:
    #     if not merged or merged[-1][1] < interval[0]:
    #         merged.append(interval)
    #     else:
    #         merged[-1][1] = max(merged[-1][1], interval[1])
    #
    # return merged
    left, right = newInterval
    res = []
    placed = False
    for li, ri in intervals:
        if li > right:
            if not placed:
                res.append([left, right])
                placed = True
            res.append([li, ri])
        elif ri < left:
            res.append([li, ri])
        else:
            left = min(li, left)
            right = max(ri, right)
    if not placed:
        res.append([left, right])
    return res


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))