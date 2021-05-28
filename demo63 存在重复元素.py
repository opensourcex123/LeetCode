# 作者：宁方笑
# 开发时间：2021/5/28 17:45
def containsDuplicate(nums):
    hash=set()
    for i in nums:
        if i in hash:
            return True
        else:
            hash.add(i)
    return False

nums=[1,2,3,4]
print(containsDuplicate(nums))