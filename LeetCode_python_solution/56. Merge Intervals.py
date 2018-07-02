'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
题意：表示范围的数组合并
思路：以start为key对数组进行排序，然后对加入结果的interval需不需要进行合并操作进行判断
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        res=[]
        for itv in intervals:
            if not res or itv.start>res[-1].end:
                res.append(itv)
            elif itv.start<=res[-1].end:
                res[-1].end=max(res[-1].end,itv.end)
        return res