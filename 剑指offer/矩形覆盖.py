'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
思路：动态规划dp[n]=dp[n-1]+dp[n-2]
'''

class Solution:
    def rectCover(self, number):
        # write code here
        if number==0 or number==1 or number==2:
            return number
        nums=[1,1]
        for i in range(2,number+1):
            nums.append(nums[-1]+nums[-2])
        return nums[-1]