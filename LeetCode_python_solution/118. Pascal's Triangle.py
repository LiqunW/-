'''
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

题意：杨辉三角小
思路：先生成头尾的1，从第三行开始，中间的数字a[i][j]=a[i-1][j-1]+a[i-1][j]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(1,numRows+1):
            cur_level=[0]*i
            cur_level[0]=1;cur_level[-1]=1
            for j in range(1,len(cur_level)-1):
                cur_level[j]=res[-1][j-1]+res[-1][j]
            res.append(cur_level)
        return res