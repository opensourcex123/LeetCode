# 作者：宁方笑
# 开发时间：2021/5/10 9:50
from math import ceil
def storeWater(bucket,vat):
    if sum(vat)==0:
        return 0
    n=len(vat)
    ans=10**4+n
    for i in range(1,10**4):
        res=i
        for j in range(n):
            res+=max(0,ceil(vat[j]/i)-bucket[j])
        ans=min(ans,res)
    return int(ans)

bucket = [16,29,42,70,42,9]
vat = [89,44,50,90,94,91]
print(storeWater(bucket,vat))