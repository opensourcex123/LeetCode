# 作者：宁方笑
# 开发时间：2021/6/11 11:07
def isBadVersion(n):
    pass
def firstBadVersion(n): #在二分查找中，选取mid的方法一般为 mid=left+right/2,(left+right)。
    # 如果使用的编程语言会有整数溢出的情况（例如 C++，Java），
    # 那么可以用mid=left+ (right−left)/2代替前者。
    left=1
    right=n
    while left<right:
        mid=(left+right)//2
        if isBadVersion(mid):
            right=mid
        else:
            left=mid+1
    return left