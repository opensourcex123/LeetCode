# 作者：宁方笑
# 开发时间：2021/6/17 15:34
def intersection(nums1, nums2):
    set1=set(nums1) #集合保证数据的单一性，同时减少了寻取的时间复杂度
    set2=set(nums2)
    res=[]
    for num in set1:
        if num in set2:
            res.append(num)
    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1,nums2))