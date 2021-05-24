# 作者：宁方笑
# 开发时间：2021/3/10 20:46
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def mergeTwoLists(l1,l2):
    L=ListNode(-1)
    p=L
    while l1 and l2:
        if l1.val<=l2.val:
            p.next=l1
            p=l1
            l1=l1.next
        else:
            p.next=l2
            p=l2
            l2=l2.next
    p.next=l1 if l1 is not None else l2
    return L.next

l1=ListNode([1,2,4])
l2=ListNode([1,3,4])
l3=mergeTwoLists(l1,l2)
print(l3)