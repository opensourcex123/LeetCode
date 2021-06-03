# 作者：宁方笑
# 开发时间：2021/6/3 16:13
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in=[]
        self.stack_out=[]


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                x=self.stack_in.pop()
                self.stack_out.append(x)
        if self.stack_out:
            res=self.stack_out.pop()
            return res
        else:
            return


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                x=self.stack_in.pop()
                self.stack_out.append(x)
        if self.stack_out:
            res = self.stack_out[-1]
            return res
        else:
            return


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack_out and not self.stack_in



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2,param_3,param_4)