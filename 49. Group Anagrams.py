'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
题意：group anagrams
思路：用一个长度为26的数组保存每个字符串的构成，相同的就放到哈希表中
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        dictmap={}
        for string in strs:
            tmp=[0]*26
            for i in string:
                tmp[ord(i)-ord('a')]+=1
            if str(tmp) not in dictmap:
                dictmap.update({str(tmp):[string]})
            else:
                dictmap[str(tmp)].append(string)
        return list(dictmap.values())

