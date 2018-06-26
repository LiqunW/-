'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
题意：两数和为特定值
思路：哈希，建表的同时进行查找，如果存在就返回idx
时间复杂度O(n)遍历了数组一遍，空间复杂度O(n)
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict={}
        for idx,num in enumerate(nums):
            if target-num in nums_dict:
                return [nums_dict[target-num],idx]
            else:
                nums_dict[num]=idx
                