'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
题意：找出最长递增子序列（不连续）
思路：
1.动态规划，状态转移方程dp[i]=max(dp[j])+1 j<=i ，对于长度为i的序列，判断他的最长子序列是多少，
然后判断i+1个元素是否大于i元素，如果大，那么i+1长度的最长子序列就要+1

2.dp+二分
维护一个递增的dp数组，二分查找每个数在单调序列中的位置，然后替换,如果比dp数组最后一个数还要大，就增加



'''

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp) if dp else 0

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        dp=[]
        for i in range(length):
            low,high=0,len(dp)-1
            while low<=high:
                mid=(high-low)//2+low
                if dp[mid]>=nums[i]:
                    high=mid-1
                else:
                    low=mid+1
            if low>=len(dp):
                dp.append(nums[i])
            else:
                dp[low]=nums[i]
        return len(dp)