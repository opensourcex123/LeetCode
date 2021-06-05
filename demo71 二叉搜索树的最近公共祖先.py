# 作者：宁方笑
# 开发时间：2021/6/5 10:36
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    ancestor = root
    while True:  # 我们从根节点开始遍历；如果当前节点的值大于 p 和 q 的值，说明 p 和 q 应该在当前节点的左子树，因此将当前节点移动到它的左子节点；如果当前节点的值小于 p 和 q的值，说明 p 和 q 应该在当前节点的右子树，因此将当前节点移动到它的右子节点；如果当前节点的值不满足上述两条要求，那么说明当前节点就是「分岔点」。此时p 和 q 要么在当前节点的不同的子树中，要么其中一个就是当前节点。
        if p.val < ancestor.val and q.val < ancestor.val:
            ancestor = ancestor.left
        elif p.val > ancestor.val and q.val > ancestor.val:
            ancestor = ancestor.right
        else:
            break
    return ancestor
