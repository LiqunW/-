'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

题意：26进制转换成10进制
思路：进制转换
'''
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0;cnt=1
        for i in s[::-1]:
            ans+=cnt*(ord(i)-ord('A')+1)
            cnt*=26
        return ans