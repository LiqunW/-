'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

题意：找出数组中只出现一次的数字（其他都出现2次）
思路：1.哈希表存储
     2.利用异或的性质，两个相同的数字异或为0，0和任何数字异或为自身

'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        res = 0
        for i in nums:
            res = res ^ i
        return res