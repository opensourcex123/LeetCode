# 作者：宁方笑
# 开发时间：2021/4/18 21:31
 class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root:TreeNode)->bool:
    if not root:
        return 0
    left=maxDepth(root.left)
    right=maxDepth(root.right)
    return maxDepth(left,right)+1