'''
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
当n超过一次循环的时候，取模
'''



class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s :
            return ''
        length=len(s)
        if n>length:
            n=n%length
        return s[n:]+s[:n]