# 作者：宁方笑
# 开发时间：2021/6/7 10:06
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):  #深度遍历
    def construct_path(root,path):
        if root:
            path+=str(root.val)
            if not root.left and root.right:
                paths.append(path)
            else:
                path+='->'
                construct_path(root.left,path)
                construct_path(root.right,path)
    paths=[]
    construct_path(root,'')
    return paths