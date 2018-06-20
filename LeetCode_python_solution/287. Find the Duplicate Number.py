'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
题意：找出长度为n+1的数组中的重复数字，数组中元素的大小为1-n，不能修改原来的数组
思路：不能用排序和哈希，二分查找的思想假设枚举的数字为 n / 2：

遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，
否则可以确定解落在(n / 2, n]范围内。

思路2：利用判断链表是否存在环的思想，通过一个每次进行一个操作的慢指针和一个每次进行两个操作的快指针进行迭代，
来找到重复元素。然后由于存在重复元素，所以一定存在两个以上的下标指向同一个数，
这就会造成多次迭代后，快慢指针一定都会进入一个循环中。在环上以不同速度的两个指针一定会在某个位置上相遇。
'''

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=1
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            cnt=0
            for i in nums:
                if i <= mid:  #注意取等号和判断的条件
                    cnt+=1
            if cnt > mid:
                high=mid-1
            else:
                low=mid+1
        return low


class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast=nums[nums[0]]
        slow=nums[0]
        while fast != slow:
            slow=nums[slow]
            fast=nums[nums[fast]]
        fast=0
        while slow !=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow