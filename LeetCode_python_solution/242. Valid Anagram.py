'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

题意：判断两个字符串所包含的元素是否一致，只是字母顺序不同
思路：哈希表统计字符串中每个字母出现的次数，判断两个字符串是否一致或者用一个26长度的list表示包含哪些字母。
'''

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        lista = [0]*26
        for i in s:
            lista[ord(i)-ord('a')]+=1
        for i in t:
            lista[ord(i)-ord('a')]-=1
        return True if lista==[0]*26 else False