# 作者：宁方笑
# 开发时间：2021/7/11 20:47
def nextGreaterElement(nums1, nums2):
    res_dict = {i: -1 for i in nums2}
    stack = []
    for i in nums2:
        if stack and i > stack[-1]:
            res_dict[stack.pop()] = i  # 保存的是对应关系
        stack.append(i)
    res = []
    for j in nums1:  # 直接查找即可找到对应的数值
        res.append(res_dict[j])
    return res


nums1 = [3, 1, 5, 7, 9, 2, 6]
nums2 = [1, 2, 3, 5, 6, 7, 9, 11]
# nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))
