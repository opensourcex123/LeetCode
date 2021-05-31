# 作者：宁方笑
# 开发时间：2021/5/31 19:21
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self,root=None):
        self.root=root
def invertTree(root):   #递归解决，递归遍历左右子树，然后进行反转交换
    if not root:
        return root
    left=invertTree(root.left)
    right=invertTree(root.right)
    root.left,root.right=right,left
    return root
