'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
题意：除法
思路：当余数出现重复的时候，说明是除不尽的，用哈希表来存储每一次得到的余数，当出现重复的数字时就停止
'''
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        #sign = '-' if numerator * denominator < 0 else ''
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        #res = [sign, str(quotient), '.']
        res = [str(quotient), '.']
        remainders = []
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            res.append(str(quotient))

        idx = remainders.index(remainder)
        res.insert(idx + 2, '(')
        res.append(')')

        ans = ''.join(res).replace('(0)', '').rstrip('.')

        return ans
a=Solution()
print(a.fractionToDecimal(5,4))