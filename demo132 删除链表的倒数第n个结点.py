# 作者：宁方笑
# 开发时间：2021/8/5 21:03
class ListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)  # 哑巴结点，用于头结点的前驱节点，使链表每个元素具有普遍性
    stack = list()

    cur = dummy
    while cur:
        stack.append(cur)
        cur = cur.next
    for i in range(n):
        stack.pop()
    prev = stack[-1]
    prev.next = prev.next.next
    return dummy.next
