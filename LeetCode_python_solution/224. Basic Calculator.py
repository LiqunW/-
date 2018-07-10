'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
题意：带括号的+-计算器
思路：遇到(就把之前的结果和符号入栈，遇到)就把当前结果中的符号加上栈中的结果
'''


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0;sign = 1;stack = []
        idx = 0
        while idx < len(s):
            if s[idx].isdigit():
                num = int(s[idx])
                # 读入n位数字，转成一个数字
                while idx < len(s) - 1 and s[idx + 1].isdigit():
                    num = num * 10 + int(s[idx + 1])
                    idx += 1
                # 把该数字加入结果
                res += sign * num
            if s[idx] == '+':
                sign = 1
            elif s[idx] == '-':
                sign = -1
            elif s[idx] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[idx] == ')':
                tmp_sign = stack.pop()
                res *= tmp_sign
                tmp_num = stack.pop()
                res += tmp_num
                sign = 1
            idx += 1
        return res
