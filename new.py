class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        res = []
        for i in range(len(nums)):
            n = nums[:i]+nums[i+1:]
            for j in self.permute(n):
                res.append([nums[i]]+j)
        return res

a=Solution()
print(a.permute([1,2,3]))