'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
思路：栈是后进先出，队列是先进先出，因此用一个栈保存顺序，另一个栈保存逆序，
顺序栈完成入队操作，逆序栈完成出队操作
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        return self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()