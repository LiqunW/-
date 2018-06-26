'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
思路：先统计有几个空格，然后把字符串变为替换后的长度，再替换
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        count=0
        for i in s:
            if i==' ':
                count+=1
        length=len(s)+count*2
        i=0
        while i < length:
            if s[i]==' ':
                s=s[:i]+'%20'+s[i+1:]
                i=i+3
            else:
                i=i+1
        return s


