'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
题意：找到最长子串，子串中每个字母出现频率大于等于k
思路：分治，先统计字符串每个字母出现频率，如果最小值都大于等于k，返回字符串长度，否则以最小值为切分点分割字符串，分治
'''
import collections
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s)<k:
            return 0
        cnt,val=collections.Counter(s).most_common()[-1]  #找到出现频率最小的那个字母
        if val>=k:
            return len(s)
        #以出现频率最小的字母划分，看子串是否符合要求
        return max(self.longestSubstring(sub_s,k) for sub_s in s.split(cnt))