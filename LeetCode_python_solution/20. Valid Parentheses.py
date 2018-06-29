'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
题意:判断括号匹配是否合法
思路：用栈解决，左括号入队，判断右括号和栈顶的左括号，如果匹配，栈顶左括号出队，栈为空说明匹配合法
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        validmap={')':'(',']':'[','}':'{'}
        pairs=[]
        for c in s:
            if c in validmap and pairs and validmap[c]==pairs[-1]:
                pairs.pop()
            else:
                pairs.append(c)
        return False if pairs else True