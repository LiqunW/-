'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
题意：找出小于n的所有素数
思路：“素数筛选法”。其思想是从小的素数开始，排除该小素数的所有倍数，直到最终剩下的全是素数。
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        primes=[True]*n
        primes[0],primes[1]=False,False
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i]=[False]*len(primes[i*i:n:i])
        return sum(primes)