# 作者：宁方笑
# 开发时间：2021/5/15 18:51
import math
class MinStack(object): #思想史构造一个辅助栈，将栈顶元素与最小值联系起来

    def    __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minStack=[math.inf]


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.minStack.append(min(self.minStack[-1],val))


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)