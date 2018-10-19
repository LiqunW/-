'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

思路：把对字符串中的每个元素都当做起始位置，把其他元素当做以后的位置，然后再同样的进行操作。这样就会得到全排列。
因为会有重复元素，所以返回结果时候要用set去掉重复的，并且按照字母顺序排列
'''


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res = []
        self.helper(ss, res, '')
        return sorted(list(set(res)))

    def helper(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i + 1:], res, path + ss[i])