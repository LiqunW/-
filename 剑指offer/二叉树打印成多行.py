'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
思路：二叉树层次遍历，用length变量记录当前层的长度，就可以输出当前层的所有节点了
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        res=[]
        if not pRoot:
            return res
        level=[pRoot]
        while level:
            length=len(level)
            res.append([level[i].val for i in range(length)])
            for i in range(length):
                tmp=level.pop(0)
                if tmp.left:
                    level.append(tmp.left)
                if tmp.right:
                    level.append(tmp.right)
        return res