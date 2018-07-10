'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
题意：给了一个排序数组，进行范围搜索
思路：二分查找，找到符合条件的数后向两头查找
'''
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        start=0;end=len(nums)-1
        res=[-1,-1]
        while start<=end:
            mid=(end-start)//2+start
            if nums[mid]==target:
                res=[mid,mid]
                while res[0]>=0 and nums[res[0]]==target:
                    res[0]-=1
                while res[1]<=len(nums)-1 and nums[res[1]]==target:
                    res[1]+=1
                res[0]+=1;res[1]-=1
                return res
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return res