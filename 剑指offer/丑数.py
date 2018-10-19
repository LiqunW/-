'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
思路：一个丑数一定是由另一个丑数乘以2，3，5得到，从1开始，得到2，3，5，然后可以得到4，6，10
相当于维护3个队列，乘以2的队列，乘以3的队列，乘以5的队列，由于队列中的丑数是有序的，因此只要记录每个
队列走到哪一步即可
'''


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index==0:
            return 0
        if index==1:
            return 1
        res=[1]
        t2=0;t3=0;t5=0 # t2表示队列2走了几步，对于6来说，2*3和3*2都可以得到，因此两个队列各前进一步，所以用3个if
        for i in range(1,index):
            next_u=min([res[t2]*2,res[t3]*3,res[t5]*5])
            res.append(next_u)
            if next_u==res[t2]*2:
                t2+=1
            if next_u==res[t3]*3:
                t3+=1
            if next_u==res[t5]*5:
                t5+=1
        return res[index-1]

a=Solution()
print(a.GetUglyNumber_Solution(8))