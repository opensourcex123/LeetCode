# 作者：宁方笑
# 开发时间：2021/9/10 20:55
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    small = ListNode()
    smallHead = small
    large = ListNode()
    largeHead = large
    while head:
        if head.val < x:
            small.next = head
            small = small.next
        else:
            large.next = head
            large = large.next
        head = head.next
    large.next = None   # 空值
    small.next = largeHead.next
    return smallHead.next