'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
题意：二叉搜索树中的公共祖先节点
思路：对于二叉搜索树，公共祖先的值一定大于等于较小的节点，小于等于较大的节点。
换言之，在遍历树的时候，如果当前结点大于两个节点，则结果在当前结点的左子树里，
如果当前结点小于两个节点，则结果在当前节点的右子树里。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if p.val>q.val:
            return self.lowestCommonAncestor(root,q,p)
        if root.val>=p.val and root.val<=q.val:
            return root
        if root.val>q.val:
            return self.lowestCommonAncestor(root.left,q,p)
        if root.val<p.val:
            return self.lowestCommonAncestor(root.right,q,p)