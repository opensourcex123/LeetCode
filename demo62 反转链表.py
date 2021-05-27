# 作者：宁方笑
# 开发时间：2021/5/27 18:19
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    pre=None
    cur=head
    while cur:
        tmp=cur.next
        cur.next=pre    #将cur指针指向前一个节点
        pre=cur
        cur=tmp    #这是cur.next已经发生变化，所以不能使用cur.next
    return pre
