'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
题意：数组的全排列
思路：dfs，遍历数组，先从数组中抽取一个数，递归计算剩余数字组成的数组n，然后将该数字与结果合并，
递归终止的条件为如果数组长度不大于1，返回[nums]
'''

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        res=[]
        for i in range(len(nums)):
            n=nums[:i]+nums[i+1:]
            for j in self.permute(n):
                res.append([nums[i]]+j)
        return res