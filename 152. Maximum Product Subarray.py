'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
题意：找出乘积最大的子数组（连续）
思路：dp的思想，维护一个局部最大值和局部最小值，由于乘法的性质，局部最小值乘以一个负数后有可能会变成最大值
'''

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        loc_max=nums[0];loc_min=nums[0]
        res=nums[0]
        for i in nums[1:]:
            if i<0:
                loc_max,loc_min=loc_min,loc_max
            loc_max=max(i,loc_max*i)
            loc_min=min(i,loc_min*i)
            res=max(res,loc_max)
        return res

a=Solution()
print(a.maxProduct([2,3,-2,4]))