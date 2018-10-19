'''
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
思路：判断第一个字符是否为正负号，字符串转整数,res=res*10 +int(i)
ord（）是获取该字符的arsii码
'''



class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        string=[i for i in s]
        if string[0]=='+':
            flag=True
            string=string[1:]
        elif string[0]=='-':
            flag=False
            string=string[1:]
        elif string[0]>'9' or string[0]<'0':
            return 0
        else:
            flag=True
        res=0
        for i in string:
            if i<'0' or i>'9':
                return 0
            else:
                res=res*10 + (ord(i)-ord('0'))
        return res if flag else -res