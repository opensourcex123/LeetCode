# 作者：宁方笑
# 开发时间：2021/5/24 14:44
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(head,val):
    sen=ListNode(0) #设置哨兵结点，用做伪头，用于删除那些需要开头就要删除的元素
    sen.next=head
    prev=sen
    cur=head
    while cur:
        if cur.val==val:
            prev.next=cur.next
        else:
            prev=cur
        cur = cur.next
    return sen.next