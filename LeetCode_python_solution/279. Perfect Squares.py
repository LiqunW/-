'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
题意：一个数可以最少分解为几个平方数的和
思路：
动态规划：dp[i]=min(dp[i-j*j]+1)  0<=j*j<=i  时间复杂度O(n * sqrt n)
数论解法：O（sqrt n） 所有自然数最多只要用四个数的平方和表示
一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等，返回的结果都相同
如果一个数除以8余7的话，那么肯定是由4个完全平方数组成

'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        for i in range(n+1):
            dp[i]=i
            j=1
            while j*j <=i:
                dp[i]=min(dp[i-j*j]+1,dp[i])
                j+=1
        return dp[n]


#数论解法
import math
class Solution2:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if (n % 8 == 7):
            return 4
        a = 0
        while a * a <= n:
            b = int(math.sqrt(n - a * a))
            if a * a + b * b == n:
                return 2 if a and b else 1
            a += 1

        return 3