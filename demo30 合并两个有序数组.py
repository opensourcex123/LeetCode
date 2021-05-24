# 作者：宁方笑
# 开发时间：2021/4/25 21:33
def merge(nums1,m,nums2,n):
    nums3=[]
    p1=0
    p2=0
    while p1<m or p2<n:
        if p1 == m:
            nums3.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            nums3.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            nums3.append(nums1[p1])
            p1 += 1
        else:
            nums3.append(nums2[p2])
            p2 += 1
    nums1[:]=nums3
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1,m,nums2,n))
