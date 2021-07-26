# 作者：宁方笑
# 开发时间：2021/7/26 18:50
class Solution(object):
    tilt=0
    def findTilt(self, root):
        def traverse(root):
            if not root:
                return 0
            left=traverse(root.left)
            right=traverse(root.right)
            self.tilt+=abs(left-right)
            return left+right+root.val
        traverse(root)
        return self.tilt
