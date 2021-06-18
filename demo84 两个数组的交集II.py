# 作者：宁方笑
# 开发时间：2021/6/18 21:23
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    len1=len(nums1)
    len2=len(nums2)
    left1,left2=0,0
    res=[]
    while left1<len1 and left2<len2:
        if nums1[left1]<nums2[left2]:
            left1+=1
        elif nums1[left1]>nums2[left2]:
            left2+=1
        else:
            res.append(nums1[left1])
            left1+=1
            left2+=1
    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1,nums2))