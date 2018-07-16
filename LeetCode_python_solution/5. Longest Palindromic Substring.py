'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
题意：最长子回文串（连续的）
思路：以s中的每个字母为回文串的中间值，分奇偶搜索最长回文串 Expand Around Center
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, L, R):
        while L >= 0 and R <= len(s) - 1:
            if s[L] == s[R]:
                L -= 1
                R += 1
            else:
                break
        return s[L + 1:R]