'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
题意：判断数组中是否存在3个递增的子数组
思路：维护两个变量a，b，其中a是当前最小的元素，b是第二小并且距离a最近的元素，
当a，b均有值，且出现第三个元素的时候，说明递增序列存在。

'''

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1,min2=None,None
        for i in nums:
            if min1 is None or i <=min1:
                min1=i
            elif min2 is None or i<=min2:
                min2=i
            else:
                return True
        return False