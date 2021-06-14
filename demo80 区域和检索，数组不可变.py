# 作者：宁方笑
# 开发时间：2021/6/14 10:57
class NumArray(object): #前缀和计算

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums=[0]
        _sums=self.sums

        for num in nums:
            _sums.append(_sums[-1]+num)


    def sumRange(self, left, right):    #优化该算法，使之时间复杂度为O(1)
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        _sums=self.sums
        return _sums[right+1]-_sums[left]