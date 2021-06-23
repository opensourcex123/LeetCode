# 作者：宁方笑
# 开发时间：2021/6/23 10:28
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        isLeafNode=lambda node:not node.left and not node.right #判断节点是否为叶子节点
        def find(node:TreeNode):
            ans=0
            if node.left:
                ans+=node.left.val if isLeafNode(node.left) else find(node.left)
            if node.right and not isLeafNode(node.right):
                ans+=find(node.right)   #寻找右子树的左子树
            return ans
        return find(root) if root else 0