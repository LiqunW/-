'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
思路：哈希存储所有字符出现的次数，然后找到出现一次的字符的最小下标
时间复杂度O(n),空间复杂度O(n)
'''
import collections
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        count=collections.Counter(s)
        for i in range(len(s)):
            if count[s[i]]==1:
                return i
        return -1