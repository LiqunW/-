'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
题意：二维数组变平
思路：剥洋葱，从外向内，指定4个方向，变量up，down，left，right表明当前指针所处位置
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res=[]
        direct=0  #0 for right 1 for down 2 for left 3 for up
        up=left=0
        down=len(matrix)-1;right=len(matrix[0])-1
        while up<=down and left<=right:
            if direct==0:
                for i in range(left,right+1):
                    res.append(matrix[up][i])
                up+=1
            elif direct==1:
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                right-=1
            elif direct==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            else:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
            direct=(direct+1)%4
        return res