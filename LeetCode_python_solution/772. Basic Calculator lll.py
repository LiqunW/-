# Time:  O(n)
# Space: O(n)

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
#
# The expression string contains only non-negative integers, +, -, *, /
# operators ,
# open ( and closing parentheses ) and empty spaces .
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
#
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
#
# Note: Do not use the eval built-in library function.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                      (operators[-1] == '*' or operators[-1] == '/'):  # 乘除法优先级更高，先计算
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':  # 遇到左括号，匹配一个右括号，计算括号内的式子
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)


a=Solution()
print(a.calculate("2*(5+5*2)/(3+(6/2+8))"))

class Solution(object):
    def calculate(self, s):
        nums=[];op=[]
        num=''
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                num += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    nums.append(int(num[::-1]))
                    num= ""
            if s[i]==')' or s[i]=='*' or s[i]=='/':
                op.append(s[i])
            elif s[i]=='+' or s[i]=='-':
                while op and op[-1]=='*' or op[-1]=='/':
                    self.compute(nums, op)
            elif s[i]=='(':
                while s[-1]!=')':
                    self.compute(nums, op)
                op.pop()
        while op:
            self.compute(nums, op)
        return op[-1]