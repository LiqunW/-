'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
题意：一个数组能否分成和相等的两个数组
思路：dp[i][j]表示，从前i个元素中挑选子序列是否能计算出和j，即j=sum/2时，d[i][j]是否为true
d[i][j] 有两种情况：
1.d[i-1][j]为true
2.d[i-1][j-nums[i]] 前i-1个元素和为j-nums[i]，加上nums[i]正好完成
'''
def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    half_sum=sum(nums)
    if half_sum%2==1:
        return False
    half_sum=half_sum//2
    dp=[[False]*(half_sum+1) for _ in range(len(nums)+1)]
    for k in range(len(nums)+1):
        dp[k][0]=True
    for i in range(1,len(nums)+1):
        for j in range(1,half_sum+1):
            dp[i][j]=dp[i-1][j]
            if j>=nums[i-1]:
                dp[i][j]= dp[i][j] or dp[i-1][j-nums[i-1]]
    return dp[-1][-1]
#空间优化
def canPartition2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    half_sum = sum(nums)
    if half_sum % 2 or len(nums) <= 1:
        return False
    else:
        half_sum = half_sum // 2
    dp = [False] * (half_sum + 1)
    dp[0] = True
    for num in nums:
        for j in range(half_sum, 0, -1):
            if j >= num:
                dp[j] = dp[j] or dp[j - num]
    return dp[-1]
print(canPartition2([1, 1, 1, 3]))
#dfs方法
class Solution:
    def canPartition(self,nums):
        self.half_sum = sum(nums)
        if self.half_sum % 2 or len(nums) <= 1:
            return False
        else:
            self.half_sum = self.half_sum // 2
        nums.sort(reverse=True)
        self.nums = nums
        return self.dfs(0,self.half_sum)

    def dfs(self,start,target):
        if target<0:
            return
        elif target==0:
            return True
        for i in range(start,len(self.nums)):
            if self.dfs(i+1,target-self.nums[i]):
                return True
        return False
a=Solution()
print(a.canPartition([1, 1, 1, 3]))

class Solution2:
    def canPartition(self,nums):
        half_sum = sum(nums)
        if half_sum % 2 or len(nums) <= 1:
            return False
        else:
            half_sum = half_sum // 2
        return self.dfs(nums,half_sum)

    def dfs(self,nums,target):
        if target<0:
            return
        elif target==0:
            return True
        for i in range(len(nums)):
            if self.dfs(nums[:i]+nums[i+1:],target-nums[i]):
                return True
        return False
a=Solution2()
print(a.canPartition([1, 1, 3, 3]))
