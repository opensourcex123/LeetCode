# 作者：宁方笑
# 开发时间：2021/5/30 20:43
from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1=deque() #两端操作的队列
        self.queue2=deque()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue2.append(x)   #先将元素进入队列2，然后将队列1的元素入到队列2中，最后1，2交换，队列1即为栈
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue2,self.queue1=self.queue1,self.queue2


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue1.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue1[0]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(3)
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2,param_4)