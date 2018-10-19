'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
题意：LIS的个数
思路：需要用两个数组，dp数组保存以num[i]结尾的LIS的长度，sub_num保存以num[i]结尾的LIS的个数

'''
class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size=len(nums)
        dp=[1]*size
        sub_num=[1]*size
        for i in range(size):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        sub_num[i]=sub_num[j] #以i结尾LIS的个数就是以j结尾LIS个数
                    elif dp[j]+1==dp[i]:  # 当这两个值相等时，LIS个数就要相加
                        sub_num[i]+=sub_num[j]
        max_val=max(dp)
        res=0
        for x,y in zip(dp,sub_num):
            if x==max_val:
                res+=y
        return res