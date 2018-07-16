'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
题意：二叉搜索树验证
思路：利用中序遍历进行验证即可，遍历一次就能知道结果
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True
        self.pre = None
        self.inorder(root)
        return self.flag

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.pre:
            self.pre = root
        else:
            if root.val <= self.pre.val:
                self.flag = False
            self.pre = root
        self.inorder(root.right)