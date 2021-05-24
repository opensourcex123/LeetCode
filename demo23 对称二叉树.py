# 作者：宁方笑
# 开发时间：2021/4/17 21:13
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root:TreeNode)->bool:
    if not root:
        return True
    def check(p:TreeNode,q:TreeNode):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return check(p.left,q.right) and check(p.right,q.left)
    return check(root.left,root.right)