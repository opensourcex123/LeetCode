# 作者：宁方笑
# 开发时间：2021/9/20 20:50
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root):
    nums = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        nums.append(node.val)
        inorder(node.right)

    def findTwoSwapper(nums):
        index1, index2 = -1, -1
        for i in range(0, len(nums) - 1):
            if nums[i + 1] < nums[i]:
                index2 = i + 1
                if index1 == -1:
                    index1 = i
                else:
                    break
        x, y = nums[index1], nums[index2]
        return x, y

    def recover(root, count, x, y):
        if not root:
            return

        if root.val == x or root.val == y:
            if root.val == x:
                root.val = y
            else:
                root.val = x
            count -= 1
            if count == 0:
                return
        recover(root.right, count, x, y)
        recover(root.left, count, x, y)

    inorder(root)
    x, y = findTwoSwapper(nums)
    recover(root, 2, x, y)