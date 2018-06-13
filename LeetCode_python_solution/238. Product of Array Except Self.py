'''
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)

题意：求成积，output[i]等于除去nums[i]之外的其他元素乘积
思路：算两次，第一次计算nums[i]左边的所有数乘积，第二次计算nums[i]右边所有数乘积。

'''

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prodL,prodR,res=1,1,[]
        for i in range(len(nums)):  #计算nums[i]左边所有数的乘积
            res.append(prodL)
            prodL*=nums[i]

        for i in range(len(nums)-1,-1,-1): # 计算nums[i]右边所有数的乘积
            res[i]*=prodR
            prodR*=nums[i]
        return res