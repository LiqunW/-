'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

题意：分解字符串，使得分解后的字符串都是回文
思路：继续开始回溯的条件是目前的结果已经是回文串。然后从后面的字符开始继续回溯
'''


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(s, [], res)
        return res

    def isPalindrome(self, s):
        return s == s[::-1]

    def helper(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], path + [s[:i]], res)