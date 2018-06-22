'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
题意：爬楼梯，一次爬一步或者两步，问有多少种方案
思路：动态规划，dp[n]=dp[n-1]+dp[n-2]
'''

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return n
        dp=[1,2];res=0
        for i in range(3,n+1):
            res=sum(dp)
            dp[0]=dp[1]
            dp[1]=res
        return res