# 作者：宁方笑
# 开发时间：2021/9/14 21:52
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    def reverse_linked_list(head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

    dummy_node = ListNode(-1)
    dummy_node.next = head
    pre = dummy_node
    for _ in range(left - 1):
        pre = pre.next

    right_node = pre
    for _ in range(right - left + 1):
        right_node = right_node.next

    left_node = pre.next
    curr = right_node.next

    pre.next = None
    right_node.next = None

    reverse_linked_list(left_node)

    pre.next = right_node
    left_node.next = curr
    return dummy_node.next
