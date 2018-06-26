'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same
color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
题意：颜色排序
思路：两次遍历很简单，
一次遍历方法，双指针，
- 定义red指针指向开头位置，blue指针指向末尾位置
- 从头开始遍历原数组，如果遇到0，则交换该值和red指针指向的值，并将red指针后移一位。若遇到2，
则交换该值和blue指针指向的值，并将blue指针前移一位。若遇到1，则继续遍历。
保证了red指针始终指向排好序的0的后一个数，blue指针始终指向排号序的2的前一个数
'''
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red=0;blue=len(nums)-1
        i=0
        while i<=blue:
            if nums[i]==0:
                nums[i],nums[red]=nums[red],nums[i]
                red+=1
                i+=1
            if nums[i]==2:
                nums[i],nums[blue]=nums[blue],nums[i]
                blue-=1
            else:
                i+=1