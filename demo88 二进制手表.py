# 作者：宁方笑
# 开发时间：2021/6/22 10:46
def readBinaryWatch(turnedOn):
    res=[]
    for h in range(12):
        for m in range(60):
            if bin(h).count("1")+bin(m).count("1")==turnedOn:
                res.append(f"{h}:{m:02d}")  #m:02d保证了可以输出两位
    return res

n=1
print(readBinaryWatch(n))
