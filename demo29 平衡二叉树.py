# 作者：宁方笑
# 开发时间：2021/4/23 21:55
def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def height(root):
        if not root:
            return 0
        return max(height(root.left),height(root.right))+1
    if not root:
        return True
    return abs(height(root.left)-height(root.right))<=1 and isBalanced(root.left) and isBalanced(root.right)    #左子树右子树的高度差小于等于1，然后递归下去