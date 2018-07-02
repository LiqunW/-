'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

题意：找到和最大的连续子序列
思路：动态规划，如果之前的和加上当前的数比当前数还要小，那么序列的头就从当前的数开始
'''


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_val = nums[0]
    local_max = nums[0]
    if len(nums)==1:
        return max_val
    for i in nums[1:]:
        local_max = max(local_max+i,i)
        max_val = max(local_max, max_val)
    return max_val

#返回该序列
import sys
class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = local_max = -sys.maxsize -1
        begin=end=0
        for i,x in enumerate(nums[0:]):
            if x > local_max + x:
                begin = i
                local_max=x
            else:
                local_max=local_max+x
            if max_val < local_max:
                end = i
                max_val=local_max
        print(begin,end)
        return max_val

a=Solution2()
a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])