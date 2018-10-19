'''
{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和(子向量的长度至少是1)
思路：用loc和gl变量分别记录当前最大和以及全局最大和
'''

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        if len(array)==1:
            return array[0]
        loc_sum=array[0]
        gl_sum=array[0]
        for i in array[1:]:
            loc_sum=max(i,i+loc_sum) # loc_sum+i<i，就舍弃之前累积的和，从当前这个数开始计算
            gl_sum=max(gl_sum,loc_sum)
        return gl_sum