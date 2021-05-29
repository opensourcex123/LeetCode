# 作者：宁方笑
# 开发时间：2021/5/29 19:32
def containsNearbyDuplicat(nums, k):
    dic={}  #维护一个字典，相当于哈希表
    for i in range(len(nums)):
        if nums[i] in dic and dic[nums[i]]>=i-k:
            return True
        else:
            dic[nums[i]]=i  #这种格式来添加字典，不一定要用字典生成式
    return False

nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicat(nums,k))