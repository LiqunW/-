'''
题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
思路：直接查找
利用性质，从右上角或者左下角开始查找，可以减少搜索时间
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        #从左下角开始查找
        row,column = len(matrix)-1,len(matrix[0])-1
        i,j=row,0
        while i>=0 and j<=column:
            if matrix[i][j]>target:
                i-=1
            elif matrix[i][j]<target:
                j+=1
            else:
                return True
        return False