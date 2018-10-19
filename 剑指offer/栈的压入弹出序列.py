'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
思路：模拟法，建立一个辅助栈，当辅助站的栈顶和出栈顺序栈顶元素一致时，出栈，否则就按照入栈顺序入栈，最后根据辅助栈是否为空判断
'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV and not popV:
            return True
        if not pushV or not popV:
            return False
        stack=[]
        for i in pushV:
            stack.append(i)
            while stack and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)
        return True if not stack else False

a=Solution()
print(a.IsPopOrder([1,2,3,4,5],[4,3,5,1,2]))
# 不使用辅助栈的方法
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV and not popV:
            return True
        if not pushV or not popV:
            return False
        pushV=pushV[::-1]
        count=0
        for i in range(len(pushV)):
            if pushV[i]==popV[i]:
                count+=1
        return True if count>0 else False