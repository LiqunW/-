'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
题意：旋转数组中的搜索
思路：二分查找，如果mid>r，说明左半边数组是有序的，先看target是否在左半边，否则搜索右边
如果mid<r，说明右半边数组有序，先看target是否在右半边，否则搜索左半边
'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0;right=len(nums)-1
        while left<=right:
            mid = (right-left)//2 + left
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[right]:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if target<nums[mid] and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
