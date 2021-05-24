# 作者：宁方笑
# 开发时间：2021/5/12 21:38
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head):
    seen=set()  #哈希集合，遍历整个列表，如果出现在表中，则证明又循环，否则没有
    while head:
        if head in seen:
            return True
        seen.add(head)
        head=head.next
    return False

head = [3,2,0,-4]
print(hasCycle(head))