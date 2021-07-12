# 作者：宁方笑
# 开发时间：2021/7/12 21:44
class Solution(object):
    def __init__(self):
        self.pre=None
        self.res=[]
        self.ret_count,self.max_count,self.cur_count=0,0,0

    def findMode(self,root):
        self.inOrder(root)
        self.pre=None
        self.ret=[0]*self.ret_count
        self.ret_count,self.cur_count=0,0
        self.inOrder(root)
        return self.ret
    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val==root.val:
            self.cur_count+=1
        else:
            self.cur_count=1
        if self.cur_count>self.max_count:
            self.max_count=self.cur_count
            self.ret_count+=1
        elif self.cur_count==self.max_count:
            if len(self.res):
                self.ret[self.ret_count]=root.val
            self.ret_count+=1
        self.pre=root
        self.inOrder(root.right)