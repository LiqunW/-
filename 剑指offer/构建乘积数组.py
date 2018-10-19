'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
思路：从左到右乘A[i]左边的数字，然后从右到左乘A[i]右边的数字
'''
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return
        B=[1]*len(A)
        for i in range(1,len(A)):
            B[i]=B[i-1]*A[i-1]
        tmp=1
        for i in range(len(A)-2,-1,-1):
            tmp*=A[i+1]
            B[i]*=tmp
        return B