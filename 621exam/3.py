import sys
'''找出最长重复字符串，例如xabcabcx中的最长重复字符串就是abcabc，返回6，如果不存在就返回0'''
class Solution:
    def longestrepeat(self,strs):
        if len(strs) <= 1:
            return 0
        res = 0
        for length in range(2, len(strs)+1, 2):
            for i in range(0, len(strs) - length+1):
                flag = self.helper(strs[i:i + length])
                if flag:
                    res = max(res, length)
        return res

    def helper(self,s):
        left = 0
        mid = len(s) // 2
        while left < len(s) // 2:
            if s[left]==s[mid]:
                left += 1
                mid += 1
            else:
                return False
        return True

#a=Solution()
#print(a.longestrepeat("xabcabcx"))
if __name__ == '__main__':
    input=str(sys.stdin.readline())
    s=Solution()
    output=s.longestrepeat(input)
    print(output)
