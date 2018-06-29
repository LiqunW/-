'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
题意：找出两条边所能盛水的最大容量
思路：从两边向中间搜索，每次移动较短的那条边
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0;right=len(height)-1
        max_val=0
        while left < len(height) and right>=0 and left<right:
            cur_val=(right-left)*min(height[left],height[right])
            max_val=max(max_val,cur_val)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_val
