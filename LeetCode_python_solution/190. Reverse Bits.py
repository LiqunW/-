'''
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
             return 964176192 represented in binary as 00111001011110000010100101000000.
题意：二进制数字的翻转
思路：原数字不断右移，将最低位给新数字，新数字不断左移
如果该方法要被调用很多次，存储每次翻转的数字和结果即可
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res=0
        for i in range(32):
            res<<=1
            res |= n&1
            n>>=1
        return res