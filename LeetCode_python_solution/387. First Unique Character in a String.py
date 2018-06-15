'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

题意：找到字符串中第一个不重复的字母的下标
思路：先统计字符串中所有字符出现的次数，然后遍历字符串，判断当前字母是否只出现了一次

'''
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=collections.defaultdict(int)
        for i in range(len(s)):
            count[s[i]]+=1
        res=-1
        for i in s:
            if count[i]==1:
                return s.index(i)
        return res
