'''

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

题意：数组能被等分成和相等的几份
'''
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums and k == 1:
            return True
        if not nums or len(nums) < k or k <= 0:
            return False
        _sum = sum(nums)
        div, mod = divmod(_sum, k)
        if mod or max(nums) > div:
            return False
        nums.sort(reverse=True)
        target = [div]*k
        return self.dfs(nums,k,0,target)

    def dfs(self, nums, k, index, target):
        if index == len(nums):
            return True
        num = nums[index]
        for i in range(k):
            if target[i] >= num:
                target[i] -= num
                if self.dfs(nums, k, index+1, target):
                    return True
                target[i] += num
        return False


a = Solution()
nums=[4, 3, 2, 3, 5, 2, 1]
print(a.canPartitionKSubsets(nums,k=4))
