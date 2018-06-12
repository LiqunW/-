'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]


题意：把数组中的0放到数组末尾，其他元素相对位置不变
思路：双指针x，y，都指向数组头部，当x指向的元素不为0时，交换x，y指向的元素。
指针x每次移动一步，当发生位置交换时候，y指针向前移动一步（保证y始终指向数组中的第一个0）
'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y=0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[y]=nums[y],nums[i]
                y+=1
