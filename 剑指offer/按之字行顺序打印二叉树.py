'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
思路：二叉树的层次遍历
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        res=[]
        if not pRoot:
            return res
        level=[pRoot];reverse=False
        while level:
            length=len(level)
            if reverse:
                res.append([level[i].val for i in range(length)][::-1])
            else:
                res.append([level[i].val for i in range(length)])
            for i in range(length):
                tmp=level.pop(0)
                if tmp.left:
                    level.append(tmp.left)
                if tmp.right:
                    level.append(tmp.right)
            reverse=not reverse
        return res