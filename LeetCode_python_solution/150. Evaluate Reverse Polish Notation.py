'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
题意：逆波兰表达式求解
思路：遇到数字就入栈，遇到运算符栈顶的两个元素出栈，注意出发的取整分正负
'''
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        if not tokens:
            return stack
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                num1=stack.pop()
                num2=stack.pop()
                if token=='+':
                    stack.append(num1+num2)
                elif token=='-':
                    stack.append(num2-num1)
                elif token=='*':
                    stack.append(num1*num2)
                elif token=='/':
                    if num1*num2<0:
                        stack.append(int(-(-num2)/num1))
                    else:
                        stack.append(int(num2/num1))
        return stack.pop()