'''
和为S的两个数字
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
因为是递增序列，因此用二分查找,当和小于tsum时，start向后移动，大于时，end向前移动，符合条件时，记录结果，并且start向前移动一步
'''

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        start=0;end=len(array)-1;sums=array[start]+array[end]
        res=[]
        while start<end:
            if sums==tsum:
                if not res:
                    res=[array[start],array[end],array[start]*array[end]]
                else:
                    if array[start]*array[end]<=res[-1]:
                        res=[array[start],array[end],array[start]*array[end]]
                start+=1
                sums=array[start]+array[end]
            elif sums<tsum:
                start+=1
                sums=array[start]+array[end]
            else:
                end-=1
                sums=array[start]+array[end]
        return res[:2] if res else []