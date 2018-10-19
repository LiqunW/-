'''
题意：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
思路：n为偶数，a^n=a^n/2*a^n/2;n为奇数，a^n=（a^（n-1）/2）*（a^（n-1/2））*a
时间复杂度为O(lgn)
循环的写法
'''
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent<0:
            base=1/base
            exponent=-exponent
        if exponent==0:
            return 1
        half=self.Power(base,exponent//2)
        if exponent%2:
            return half*half*base
        else:
            return half*half

class Solution2:
    def Power(self,base,exponent):
        if exponent<0:
            base=1/base
            exponent=-exponent
        if exponent==0:
            return 1
        res=1
        while exponent>0:
            if exponent//2:
                res*=base
            base*=base
            exponent=exponent//2
        return res
