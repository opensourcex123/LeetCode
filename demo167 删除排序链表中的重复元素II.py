# 作者：宁方笑
# 开发时间：2021/9/9 19:27
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return head

    dummy = ListNode(0, head)

    cur = dummy
    while cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            x = cur.next.val
            while cur.next and x == cur.next.val:
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next
