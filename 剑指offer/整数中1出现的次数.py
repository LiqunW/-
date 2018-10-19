'''
从1 到 n 中1出现的次数
思路：找规律
1)此位大于1，这一位上1的个数有 ([n / 10^(b+1) ] + 1) * 10^b
    2)此位等于0，为 ([n / 10^(b+1) ] ) * 10^b
    3)此位等于1，在0的基础上加上n mod 10^b + 1

    举个例子：


    30143:
    由于3>1,则个位上出现1的次数为(3014+1)*1
    由于4>1,则十位上出现1的次数为(301+1)*10
    由于1=1，则百位上出现1次数为(30+0)*100+(43+1)
    由于0<1，则千位上出现1次数为(3+0)*1000

注:以百位为例，百位出现1为100~199，*100的意思为单步出现了100~199，100次，
*30是因为出现了30次100~199,+(43+1)是因为左后一次301**不完整导致。

https://blog.csdn.net/ns_code/article/details/27563485
'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n<=0:
            return 0
        count=0
        #base 当前位的基 remain 当前位为1时，后面位剩余的数中1出现的次数
        base=1;remain=0
        while n:
            current=n%10 # 当前位
            n=n/10
            if current>1:
                count+=(n+1)*base
            elif current==1:
                count+=n*base+(remain+1)
            else:
                count+=n*base
            remain+=current*base
            base*=10
        return count
