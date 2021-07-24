# 作者：宁方笑
# 开发时间：2021/7/24 20:52
def maxDepth(root): #N叉树不一定有多少个子节点，深度遍历递归解决，分三种情况
    if not root:
        return 0
    elif root.children==[]:
        return 1
    else:
        height=[maxDepth(c) for c in root.children]
    return max(height)+1