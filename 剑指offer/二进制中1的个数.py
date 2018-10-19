'''
题意：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
思路：如果是负数，和32位1与，把最高位变为符号位，n-1和 n 与，每次运算都去掉了最低位的1
'''


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count

a=Solution()
print(a.NumberOf1(9999))