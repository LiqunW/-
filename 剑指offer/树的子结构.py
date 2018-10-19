'''
题意：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
思路：首先要找到A数中和B数root节点相同的节点，然后再判断以该节点为root的A子树是否和B树相同
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res = False
        if pRoot1 and pRoot2: # 空树不是任意一个树的子结构
            if pRoot1.val == pRoot2.val: # 先找到相同的root节点，再判断
                res = self.isSub(pRoot1, pRoot2)
            if res == False:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            if res == False:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        return res

    def isSub(self, root1, root2):
        if not root2: # B树为空，说明所有结构都一样，True
            return True
        if not root1: # A空，B非空，结构不一致
            return False
        if root1.val != root2.val:
            return False
        return self.isSub(root1.left, root2.left) and self.isSub(root1.right, root2.right) 
