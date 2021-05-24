# 作者：宁方笑
# 开发时间：2021/5/20 21:12
def trailingZeroes(n):
    count=0
    while n>0:  #时间复杂度为O(nlogn)
        n//=5
        count+=n
    return count

n=6836
print(trailingZeroes(n))