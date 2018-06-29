'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
题意：根据中序和后续遍历结果重建二叉树
思路：和105题一样，root在后序遍历的最后一个节点
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return
        root=TreeNode(postorder[-1])
        idx=inorder.index(root.val)
        root.left=self.buildTree(inorder[:idx],postorder[:idx])
        root.right=self.buildTree(inorder[idx+1:],postorder[idx:len(postorder)-1])
        return root