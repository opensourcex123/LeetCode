# 作者：宁方笑
# 开发时间：2021/4/16 21:22
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):   #定义树的节点
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p:TreeNode,q:TreeNode)->bool:    #深度优先搜索
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val!=q.val:
        return False
    else:
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
