'''
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
思路：如果第二个字符不是*，那么s和pattern都向后移动一位
如果第二个字符是*，分三种情况：1.pattern向后移动两位，相当于忽略x*
                         2.s后移一位，pattern后移两位
                         3.s后移一位，pattern不变，
'''



class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s==pattern:
            return True
        if len(pattern)>1 and pattern[1]=='*':
            if s and (s[0]==pattern[0] or pattern[0]=='.'):
                return self.match(s,pattern[2:]) or self.match(s[1:],pattern)
            else:
                return self.match(s,pattern[2:]) # *前的字符串被忽略
        elif s and pattern and (s[0]==pattern[0] or pattern[0]=='.'):
            return self.match(s[1:],pattern[1:])
        return False