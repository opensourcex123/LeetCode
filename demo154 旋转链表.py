# 作者：宁方笑
# 开发时间：2021/8/27 21:16
def rotateRight(head, k):
    if k == 0 or not head or not head.next:
        return head

    n = 1
    cur = head
    while cur.next:
        cur = cur.next
        n += 1

    if (add := n - k % n) == n:
        return head
    cur.next = head  # 将链表连接成闭合链表

    while add:  # 找到闭合链表的最后一个结点
        cur = cur.next
        add -= 1

    res = cur.next
    cur.next = None
    return res


