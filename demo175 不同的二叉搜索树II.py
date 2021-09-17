# 作者：宁方笑
# 开发时间：2021/9/17 20:59
class TreeNode():
    pass

def generateTrees(n):   # 回溯法
    def generateTree(start, end):
        if start > end:
            return [None, ]

        allTrees = []
        for i in range(start, end + 1):
            leftTrees = generateTree(start, i - 1)
            rightTrees = generateTree(i + 1, end)
            for l in leftTrees:
                for r in rightTrees:
                    currTree = TreeNode(i)
                    currTree.left = l
                    currTree.right = r
                    allTrees.append(currTree)
        return allTrees

    return generateTree(1, n) if n else []