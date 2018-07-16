'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
题意：最长不含重复字母的子串
思路：从头开始遍历，用两个指针表示符合条件的字符串的头尾，end指针每次向后移动一步，当出现重复字符串时，start指针
向后移动，直到指向重复字符的后一个字符为止。
'''
import collections
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=end=0
        res=0
        count=collections.defaultdict(int)
        for c in s:
            end+=1
            count[c]+=1
            while count[c]>1:
                count[s[start]]-=1
                start+=1
            res=max(res,end-start)
        return res