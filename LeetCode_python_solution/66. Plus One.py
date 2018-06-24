'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
题意：数字加1，按照list的形式返回
思路：先提取数组，然后加1，在变成数组
从后往前，直接在数组上加1，遇到10要进位，当第一位为10的时候，在数组头插入一个1
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        Flag = True
        idx = len(digits) - 1
        while Flag and idx>-1:
            digits[idx] = digits[idx] + 1
            if digits[idx] == 10:
                digits[idx]=0
                Flag = True
                idx -= 1
            else:
                break
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits