# 作者：宁方笑
# 开发时间：2021/8/24 21:01
def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
