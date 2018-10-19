'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
思路：用两个list来模拟栈操作，stack存储入栈的数，stack_min存储当前stack中的最小值
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack=[]
        self.stack_min=[]
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.stack_min or node<=self.stack_min[-1]:
            self.stack_min.append(node)
    def pop(self):
        # write code here
        tmp=self.stack.pop()
        if tmp==self.stack_min[-1]:
            self.stack_min.pop()
        return tmp
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.stack_min[-1]