'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
题意：给定一个数字，求所有正确的括号组合
思路：全排列，用dfs
当右边的括号数量比左边大的时候，肯定是不合法的括号组合，去除，因此判断条件为L>R，
当L和R均为0时，完成匹配，将该结果加入
'''


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        if n <= 0:
            return []
        self.dfs(n, n, '')
        return self.res

    def dfs(self, L, R, item):
        if L > R:
            return
        if L == 0 and R == 0:
            self.res.append(item)
        if L > 0:
            self.dfs(L - 1, R, item + '(')
        if R > 0:
            self.dfs(L, R - 1, item + ')')

