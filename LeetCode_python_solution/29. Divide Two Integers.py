'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
题意：除法的实现
思路：用加法来代替除法
'''
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend>0 and divisor<0 or dividend<0 and divisor>0:
            flag=True
            if abs(dividend) < abs(divisor):
                return 0
        else:
            flag=False
        sums=0;count=0;res=0
        divid=abs(dividend);divis=abs(divisor)
        while divid>=divis:
            sums=divis
            count=1
            while sums+sums <= divid: # 二分搜索的思想，如果和比被除数小，就一直加，直到和大于被除数的一半
                sums+=sums
                count+=count
            #被除数每次都减小一半
            divid-=sums
            res+=count
        if flag:
            return max(0-res, -2**31)
        else:
            return min(res,2**31-1)