'''
如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
思路：先统计一下0，然后统计不连续的牌直接的间隔是多少，如果能用0填充，则True 否则False
'''



class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers)<5:
            return False
        numbers.sort()
        zero_cnt=numbers.count(0);gap=0
        L=zero_cnt
        R=zero_cnt+1
        while R<=len(numbers)-1:
            if numbers[L]==numbers[R]:
                return False
            else:
                gap+=numbers[R]-numbers[L]-1
            L+=1;R+=1
        return True if gap<=zero_cnt else False