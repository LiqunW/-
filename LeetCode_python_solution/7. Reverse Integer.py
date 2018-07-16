'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
题意：数字翻转，溢出返回0
思路：每次取出原数字的末位，res=res*10+该数字
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1

        x = abs(x)
        res = 0
        length = len(str(x))
        while length > 0:
            res = res * 10 + x % 10
            x = x // 10
            length -= 1
        if sign * res > 2 ** 31 or sign * res < -2 ** (32 - 1):
            return 0
        else:
            return sign * res