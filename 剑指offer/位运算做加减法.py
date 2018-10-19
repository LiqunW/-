'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
思路：与运算求进位，异或运算用来求和，左移运算用来把进位加到结果中
'''


class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            carry=(num1 & num2)
            num1=(num1 ^ num2) % 0x100000000
            num2=(carry<<1) % 0x100000000
        return num1 if num1 < 0x7FFFFFFF else num1 | (~0x100000000+1)