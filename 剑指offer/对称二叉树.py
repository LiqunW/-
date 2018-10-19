'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
思路：递归判断二叉树的节点交换后是否相等就可以
'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isSymmetry(pRoot.left, pRoot.right)

    def isSymmetry(self, Root1, Root2):
        if not Root1 and not Root2: # 两个节点都为空，说明判断结束
            return True
        if not Root1 or not Root2:
            return False
        if Root1.val != Root2.val:
            return False
        return self.isSymmetry(Root1.left, Root2.right) and self.isSymmetry(Root1.right, Root2.left)
