'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
题意：happy number
思路：模拟法，用set存储每次计算后的n，如果n出现过且不为1，则False，如果n=1，则True
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=set()
        while n!=1:
            num.add(n)
            sums=sum(int(i)**2 for i in str(n))
            n=sums
            if n in num:
                return False
        return True