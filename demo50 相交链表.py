# 作者：宁方笑
# 开发时间：2021/5/15 20:59
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hash=set()
        A=headA
        B=headB
        while A!=None:
            hash.add(A)
            A=A.next
        while B!=None:
            if B in hash:
                return B
            B=B.next
        return None