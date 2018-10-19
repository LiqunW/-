'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
题意：计算器
思路：需要考虑优先级。使用一个栈保存数字，如果该数字之前的符号是加或减，
那么把当前数字压入栈中，注意如果是减号，则加入当前数字的相反数，因为减法相当于加上一个相反数。
如果之前的符号是乘或除，那么从栈顶取出一个数字和当前数字进行乘或除的运算，再把结果压入栈中，
那么完成一遍遍历后，所有的乘或除都运算完了，再把栈中所有的数字都加起来就是最终结果了
'''
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        pre_op='+'  #保存先前的运算符
        num=0
        for i,string in enumerate(s):
            if string.isdigit():
                num=10*num+int(string)
            if i==len(s)-1 or string in '+-*/':
                # 遇到运算符的时候再做操作，因为遇到第一个操作的时候肯定是把之前的数字放到stack中，所以是对pre_op做判断
                if pre_op=='+':
                    stack.append(num)
                elif pre_op =='-':
                    stack.append(-num)
                elif pre_op=='*':  # 乘法和除法的优先级最高，所以先计算
                    stack.append(stack.pop()*num)
                elif pre_op=='/':
                    top=stack.pop()
                    if top<0:
                        stack.append(int(top/num))
                    else:
                        stack.append(top//num)
                pre_op=string
                num=0
        return sum(stack)