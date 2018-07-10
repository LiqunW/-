'''

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
题意：开根号
思路：二分查找，注意边界情况
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=1;right=x//2
        while left<=right:
            mid=(right-left)//2+left
            if mid*mid<x: # mid平方小，+1后又大，说明mid即为所求
                if (mid+1)*(mid+1)>x:
                    return mid
                left=mid+1
            elif mid*mid>x: #mid平方大，-1后又小，说明mid-1即为所求
                if (mid-1)*(mid-1)<x:
                    return mid-1
                right=mid-1
            else: # 把相等的情况都放一起
                return mid
        return x