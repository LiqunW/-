'''
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
题意：排序问题
思路：先对数组排序，然后把数组分成两半，数组的奇数部分倒序插入数组前半部分的元素，
数组的偶数部分倒序插入数组后半部分元素 时间复杂度O(nlogn),空间复杂度O(n)
'''
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        nums.sort()
        med = (len(nums)-1)//2
        nums[::2],nums[1::2]=nums[med::-1],nums[:med:-1]
        