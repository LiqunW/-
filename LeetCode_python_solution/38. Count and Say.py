'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
题意：根据上一个字符串生成下一个字符串，例如 数字1 对应'1'，下一个字符串就是1个1，因此'11'
在下一个字符串就是两个1, '21'
思路：用pre保存上一个字符，然后遍历上一个字符串，生成新的字符串
'''
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res='1'
        for i in range(n-1):
            new,count,pre='',0,res[0]
            for j in range(len(res)):
                if pre==res[j]:
                    count+=1
                else:
                    new+=str(count)+pre
                    count=1
                    pre=res[j]
            res=new+str(count)+pre
        return res