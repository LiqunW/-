'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
题意：0所在的行和列均置0
思路：O(m+n)的方法，分别用m和n长度的一维数组保存哪些位置要置0，行或列有一个成立，就要置0
'''

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        rows=[False for i in range(row)]
        column=[False for i in range(col)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    rows[i]=True;column[j]=True
        for i in range(row):
            for j in range(col):
                if rows[i] or column[j]:
                    matrix[i][j]=0