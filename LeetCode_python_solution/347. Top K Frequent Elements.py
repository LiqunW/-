'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

题意：返回出现频率最高的k个数
思路：哈希表统计，桶排序

'''

# 桶排序，时间复杂度O(n)
import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        cntDict = collections.defaultdict(int)
        for i in nums:
            cntDict[i]+=1
        freqList = [[] for i in range(n+1)]  #用来存放出现的数字，下标是该数字出现的次数
        for p in cntDict:
            freqList[cntDict[p]] += p,
        ans=[]
        for p in range(n,0,-1):   #逆序遍历freqList，找出k个出现频率最大的数字
            ans+=freqList[p]
        return ans[:k]

if __name__ == '__main__':
    a=Solution()
    a.topKFrequent(nums=[1,1,1,1,2,2,5,3],k=2)