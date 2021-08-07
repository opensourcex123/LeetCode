# 作者：宁方笑
# 开发时间：2021/8/7 21:19
class ListNode:
    def __init__(self,val,next):
        self.val=val
        self.next=next

def swapPairs(head):    #递归
    if not head or not head.next:
        return head
    newHead = head.next
    head.next = swapPairs(newHead.next)
    newHead.next = head
    return newHead