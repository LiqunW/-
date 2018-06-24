'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

题意：判断一二叉树是不是对称的
思路：二叉树的镜像是不是本身。
非递归：逐层遍历，用队列存储，每次pop队列的头和尾，判断是否相等
递归：停止条件：左右字树均为空，每次判断left.left与right.right和left.right与right.left是否相等
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left or not right:
            return left == right    #有一个节点为空，判断另一个节点是否也为空，是就返回True
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)