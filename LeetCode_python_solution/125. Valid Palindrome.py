'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
题意：回文判断，只小写字母
思路：双指针的思路
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1:
            return True
        start = 0
        end = len(s) - 1
        while start<=end and start<=len(s)-1 and end>=0:
            string1=''
            while string1=='' and start<=len(s)-1:
                if 0 <= ord(s[start]) - ord('a') <= 26:
                    string1 = s[start]
                elif 0 <= ord(s[start]) - ord('A') <= 26:
                    string1 = s[start].lower()
                elif 0 <= ord(s[start]) - ord('0') <= 9:
                    string1=s[start]
                else:
                    start += 1
            string2=''
            while string2 == '' and end>=0:
                if 0 <= ord(s[end]) - ord('a') <= 26:
                    string2 = s[end]
                elif 0 <= ord(s[end]) - ord('A') <= 26:
                    string2 = s[end].lower()
                elif 0 <= ord(s[end]) - ord('0') <= 9:
                    string2=s[end]
                else:
                    end -= 1
            if string1 != string2:
                return False
            start+=1
            end-=1
        return True
