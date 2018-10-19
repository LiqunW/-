'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
思路：设定4个方向，从左往右，从上往下，从右往左，从下往上，然后循环直到left>right,up>down
'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix)==0:
            return matrix
        row=len(matrix);col=len(matrix[0])
        left=0;right=col-1;up=0;down=row-1
        direction=0;res=[]
        while left<=right and up<=down:
            if direction==0:
                for i in range(left,right+1):
                    res.append(matrix[up][i])
                up+=1
            elif direction==1:
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                right-=1
            elif direction==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            else:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
            direction=(direction+1)%4
        return res