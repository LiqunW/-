'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
题意：返回一个能组成的最大数
思路：排序问题，对于两个字符串，如果int(a+b)<int(b+a)，那么b就要排在a的前面
'''


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(k) for k in nums]
        for i in range(len(nums)):
            for j in range(i):
                if self.smaller(nums[j], nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        res = ''.join(nums).lstrip('0')
        return res or '0'

    def smaller(self, a, b):
        if int(a + b) > int(b + a):
            return False
        else:
            return True

#python2 的解法，用到了cmp函数
class Solution2(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num=[str(x) for x in nums]
        num.sort(cmp=lambda x,y:cmp(y+x,x+y))
        return ''.join(num).lstrip('0') or '0'