'''
和为s的连续正数序列
从1开始累计，最小的是1，2这个序列，start，end分别代表序列的头和尾，当序列和小于tsum的时候，end+1，sum+end
当sum==目标时，记录结果，并且end+1，sum+end，然后就会向后搜索符合条件的序列，终止条件是end<=(target+1)/2
'''


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res=[]
        start=1;end=2;sums=3
        while end<=(tsum+1)/2:
            if sums==tsum:
                res.append(range(start,end+1))
                end+=1
                sums+=end
            elif sums<tsum:
                end+=1
                sums+=end
            else:
                sums-=start
                start+=1
        return res