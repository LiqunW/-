'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
题意：给一个无符号整数，返回这个数的二进制值里有多少个1
思路：转换成二进制，然后统计有多少个1

该方法又叫Brian Kernighan方法。当原数不为0时，将原数与上原数减一的值赋给原数。
因为每次减一再相与实际上是将最左边的1给消去了，所以消去几次就有几个1。
比如110，减去1得101，相与得100，消去了最左边的1。
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            n=n&0x7FFFFFFF  #默认所有的数都是无符号整数，因此需要去掉符号位
        count=0
        while n:
            count+=1
            n=(n-1)&n
        return count
