# 作者：宁方笑
# 开发时间：2021/4/22 21:41
import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def hasPathSum(root: TreeNode, sum: int) :
    if not root:
        return False
    queue_node=collections.deque([root])
    queue_val=collections.deque([root.val])
    while queue_node:
        now=queue_node.popleft()
        temp=queue_val.popleft()
        if not now.left and not now.right:
            if temp==sum:
                return True
            continue
        if now.left:
            queue_node.append(now.left)
            queue_val.append(now.left+temp)
        if now.right:
            queue_node.append(now.right)
            queue_val.append(now.right+temp)
    return False
