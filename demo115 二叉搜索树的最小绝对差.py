# 作者：宁方笑
# 开发时间：2021/7/19 21:18

class Solution(object):
    pre = -1
    ans = float('inf')
    def getMinimumDifference(self, root):

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.pre==-1:
                self.pre=root.val
            else:
                self.ans=min(self.ans,root.val-self.pre)   #二叉树中的最小值一定是相邻两个数的差值的最小值
                self.pre=root.val
            dfs(root.right)

        dfs(root)
        return self.ans
