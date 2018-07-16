'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
题意：实现Pow(x,n)
思路：用递归来折半计算，每次把n缩小一半，这样n最终会缩小到0，任何数的0次方都为1，
这时候我们再往回乘，如果此时n是偶数，直接把上次递归得到的值算个平方返回即可，如果是奇数，则还需要乘上个x的值。
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        half=self.myPow(x,n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x
a=Solution()
print(a.myPow(2.0,3))

#循环的解法 n每次也是减小一半，看n是否是2的倍数，是res*x，不是x*x
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x=1/x
            n=-n
        res=1
        while(n>0):
            if n%2:
                res*=x
            x*=x
            n=n//2
        return res