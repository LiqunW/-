'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
题意：输出数组中出现超过一半的数
思路：利用快排的思想，不断减小待排序的数，直到数组中的数字唯一
思路2：对数组排序，因为多数元素一定存在，且超过总个数的一半，那么排序后最中间的那个元素一定是多数元素
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res=0
        self.sort(nums)
        return self.res
    def sort(self,nums):
        if len(set(nums)) == 1:
            self.res=nums[0]
            return
        L, R, M = [], [], []
        num = nums[0]; length = len(nums)
        for i in nums:
            if i == num:
                M.append(i)
            elif i > num:
                R.append(i)
            else:
                L.append(i)
        if 2 * len(L) > length:
            self.majorityElement(L)
        elif 2 * len(R) > length:
            self.majorityElement(R)
        else:
            self.majorityElement(M)