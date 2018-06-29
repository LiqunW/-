'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
题意：组合问题
思路：dfs穷举（用递归来做）
也可以用3个循环
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dict_map = {'2': ['a', 'b', 'c'],
                         '3': ['d', 'e', 'f'],
                         '4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'],
                         '6': ['m', 'n', 'o'],
                         '7': ['p', 'q', 'r', 's'],
                         '8': ['t', 'u', 'v'],
                         '9': ['w', 'x', 'y', 'z']
                         }
        self.res = []
        if not digits:
            return self.res
        self.dfs(0, digits, '')
        return self.res

    def dfs(self, num, digits, string):
        if num == len(digits):
            self.res.append(string)
            return
        for letter in self.dict_map[digits[num]]:
            self.dfs(num + 1, digits, string + letter)
a=Solution()
a.letterCombinations('23')


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        numToCharsMap = {
            '1': [''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        result = numToCharsMap[digits[0]]
        for i in range(1, len(digits)):
            curr_result = []
            chars = numToCharsMap[digits[i]]
            for r in result:
                for char in chars:
                    curr_result.append(r + char)

            result = curr_result
        return result