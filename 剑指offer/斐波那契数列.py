'''
题意：输出斐波那契数列的第n项
思路：递归和循环fn=f(n-1)+f(n-2)
'''
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=0:
            return 0
        if n==1 or n==2:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)

class Solution2:
    def Fibonacci(self, n):
        # write code here
        # 因为只需要输出第n项，记录前一项即可，不需要保存所有的值
        if n<=0:
            return 0
        prev=0;cur=1
        for i in range(1,n):
            prev,cur=cur,prev+cur
        return cur