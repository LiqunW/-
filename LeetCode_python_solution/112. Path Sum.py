'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

题意：路径为某一数值
思路：dfs
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return True if root.val==sum else False
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)

root=TreeNode(-2)
root.right=TreeNode(-3)

class Solution2(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root,sum)
    def dfs(self,root,target):
        if not root:
            return False
        if not root.left and not root.right:
            return True if target==root.val else False
        return self.dfs(root.left,target-root.val) or self.dfs(root.right,target-root.val)


a=Solution2()
print(a.hasPathSum(root,-5))

