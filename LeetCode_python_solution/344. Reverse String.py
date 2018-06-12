'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

题目：给一个字符串，把字符串反转输出。
思路：使用把指针指向字符串末尾，倒序输出即可
'''


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]