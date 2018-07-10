'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
题意：单词搜索，不能重复使用单词
思路：dfs
'''


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == '':
            return True

        for row in range(len(board)):
            for col in range(len(board[0])):
                res = self.dfs(board, row, col, word)
                if res:
                    return True
        return False

    def dfs(self, board, i, j, word):
        if word == '':
            return True
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
            return False

        elif board[i][j] == word[0]:
            board[i][j] = '#'
            res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i, j + 1, word[1:]) \
                  or self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i, j - 1, word[1:])
            board[i][j] = word[0]
            return res