'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
题意：找到最长共同的子串
思路：横向遍历或者纵向遍历都可以
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix=strs[0]
        for i in range(1,len(strs)):
            if not prefix:
                return ''
            while prefix and strs[i][:len(prefix)] !=prefix:
                prefix=prefix[:len(prefix)-1]
        return prefix

class Solution2:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        prefix=''
        idx=0
        while idx<len(strs[0]):
            tmp=strs[0][:idx+1]
            for string in strs[1:]:
                if idx>len(string)-1 or tmp!=string[:idx+1]:
                    return prefix
            prefix=tmp
            idx+=1
        return prefix
a=Solution2()
a.longestCommonPrefix(["flower","flow","flight"])