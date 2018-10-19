'''
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
两个相同的数字异或为0，先求出两个数的异或，然后分开这两个数字
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        two_xor=0
        for i in array:
            two_xor = two_xor ^ i
        mask=1
        while two_xor & mask ==0: # 找到两个数异或之后最低位的1，说明两个数在这一位上是不同的，因此有办法分开这两个数
            mask=mask<<1
        num1=num2=0
        for i in array:
            if i & mask ==0: #其中一个数字和mask与结果为0，另一个结果不为0，就可以分开
                num1^=i
            else:
                num2^=i
        return [num1,num2]
a=Solution()
a.FindNumsAppearOnce([2,2,5,7])