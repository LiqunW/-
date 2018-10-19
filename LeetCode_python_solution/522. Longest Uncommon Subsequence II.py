'''
Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
对于多个字符串，判断最长不同的子串
思路：先对字符串按照长度排序，用集合保存已经访问的字符串，对于当前字符串s，如果出现超过一次，加入集合中，然后跳过，
如果该字符串只出现了一次，判断该字符串是否是集合中任意字符串的子集，如果不是，返回该长度
则该字符串就是最长不同子串
'''
import collections


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key=lambda x: len(x), reverse=True)
        str_dict = collections.defaultdict(int)
        visited = set()
        for s in strs:
            str_dict[s] += 1
        for s in strs:
            if str_dict[s] > 1:
                visited.add(s)
            else:
                if not visited:
                    return len(s)
                else:
                    flag = True
                    for vs in visited:
                        if self.isSubsequence(s, vs):
                            visited.add(s)
                            flag = False
                            break
                    if flag:
                        return len(s)
        return -1

    def isSubsequence(self, s, t):
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

a=Solution()
print(a.findLUSlength(["abcabc","abcabc","abcabc","abc","abc","aab"]))