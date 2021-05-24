# 作者：宁方笑
# 开发时间：2021/5/14 12:08
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
       def postOrder(root):
           if not root:
               return
           postOrder(root.left)
           postOrder(root.right)
           res.append(root.val)
       res=list()
       postOrder(root)
       return res