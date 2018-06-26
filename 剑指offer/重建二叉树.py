'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
思路：先在前序遍历中找到root节点，然后找出root节点在中序遍历中的位置，
以此把二叉树分成左右子树，然后递归建立二叉树
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return
        root=TreeNode(pre[0])
        tin_root=tin.index(pre[0])
        root.left=self.reConstructBinaryTree(pre[1:tin_root+1],tin[:tin_root])
        root.right=self.reConstructBinaryTree(pre[tin_root+1:],tin[tin_root+1:])
        return root