# 作者：宁方笑
# 开发时间：2021/6/4 9:33
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head): #通过列表使得时间复杂度为O（1）
    val=[]
    cur=head
    while cur:
        val.append(cur.val)
        cur=cur.next
    return val==val[::-1]