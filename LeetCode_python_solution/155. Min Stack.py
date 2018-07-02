'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
题意：堆栈的实现，取当前堆栈的最小值
思路：用list来模拟操作，建立一个min_stack存放当前栈中的最小值，入栈时候如果min_stack为空或者当前元素小于等于栈顶，
x入栈，出栈时如果出栈元素为min_stack栈顶元素，min_stack也要出栈
'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if not self.min_data or x <= self.min_data[-1]:
            self.min_data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        num = self.data.pop()
        if num == self.min_data[-1]:
            self.min_data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_data[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()