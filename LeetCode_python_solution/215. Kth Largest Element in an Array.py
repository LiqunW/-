'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
题意：找出数组中第k大的数
思路：快速选择法，把数组分成小于某个数和大于某个数的两个数组 O(n)，最差是O(n^2)
排序(nlogn)
'''
import random
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target=random.choice(nums)
        left,right=[],[]
        for num in nums:
            if target < num:
                left.append(num)
            elif target > num:
                right.append(num)
        if k<=len(left):
            return self.findKthLargest(left,k)
        if k>len(nums)-len(right):
            return self.findKthLargest(right,k-(len(nums)-len(right)))
        return target