'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
题意：求三个数的和为0的所有可能
思路：
1，先将数组排序。
2，排序后，可以按照TwoSum的思路来解题。怎么解呢？可以将num[i]的相反数即-num[i]作为target，
然后从i+1到len(num)-1的数组元素中寻找两个数使它们的和为-num[i]就可以了。下标i的范围是从0到len(num)-3。
3，这个过程要注意去重。
4，时间复杂度为O(N^2)。
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0:  #增加一个判断，三个正数的和不可能为0
                break
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1; right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1; right -= 1
                        while left < right and nums[left] == nums[left-1]: left +=1
                        while left < right and nums[right] == nums[right+1]: right -= 1
                    elif nums[left] + nums[right] < -nums[i]:
                        left += 1
                    else:
                        right -= 1
        return res