'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
题意：最长回文子序列（不需要连续）
思路：动态规划，dp[i][j]表示区间[i,j]区间内字符串最长回文子序列，
因此有递推公式dp[i][j]=dp[i+1][j-1]+2 if s[i]==s[j] else max(dp[i+1][j],dp[i][j-1])
'''

class Solution:
    def longestPalindromeSubseq(self, s):
        dp=[[0]*len(s) for i in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    dp[i][j]=dp[i-1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]
