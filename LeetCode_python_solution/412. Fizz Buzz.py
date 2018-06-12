'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

题意:输出1-n范围的数字，遇到3的倍数输出Fizz，遇到5的倍数输出Buzz，遇到3和5的倍数输出FizzBuzz
思路：判断当前数字能否被3，5整除


'''

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            if i % 3 ==0:
                if i % 5 == 0:
                    res.append('FizzBuzz')
                else:
                    res.append('Fizz')
            elif i % 5 ==0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res