'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
题意：找出最长连续序列
思路：排序
对暴力搜索进行改进，先把所有的数存入hashset中，使得查找的时间复杂度为O(1)，对数组中的每个数
先判断它是否是连续序列的头(num-1不在hashset中)，然后再判断以该数为起始的序列有多长
'''

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        numset=set(nums)
        longest=0
        for num in nums:
            if num-1 not in numset:
                curnum=num
                length=1
                while curnum+1 in numset:
                    curnum+=1
                    length+=1
                longest=max(longest,length)
        return longest