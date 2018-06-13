'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

题意：不用加减运算计算两数之和
思路：用位操作。将加法和进位分开计算

759+674

1. 如果我们不考虑进位，可以得到323

2. 如果我们只考虑进位，可以得到1110

3. 我们把上面两个数字假期323+1110=1433就是最终结果了

在二进制下来看，不考虑进位的加，0+0=0， 0+1=1, 1+0=1， 1+1=0，这就是异或的运算规则.
如果只考虑进位的加0+0=0, 0+1=0, 1+0=0, 1+1=1，而这其实这就是与的运算.
而第三步在将两者相加时，我们再递归调用这个算法，终止条件是当进位为0时，我们直接返回第一步的结果

对于python代码而言，需要做一些特殊处理
将一个数对0x100000000，希望该数的二进制表示从第32位开始到更高的位都同是0（最低位是第0位），
以在0-31位上模拟一个32位的int
0xFFFFFFFF 是2^32，0x7FFFFFFF是32位有符号最大整数
'''
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            carry=a&b
            a=(a^b) % 0xFFFFFFFF
            b=(carry<<1) % 0xFFFFFFFF
        return a if a < 0x7FFFFFFF else a | (~0xFFFFFFFF+1)
