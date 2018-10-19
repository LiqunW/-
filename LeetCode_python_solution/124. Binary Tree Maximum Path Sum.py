'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

题意：二叉树中的最大路径
思路：dfs
对于任意的节点A，A左右两个子节点，以左子节点为起点的最大路径是left_val,右right_val,最大路径有4种可能
1.left_val,right_val<0，那么最大路径就是A节点本身
2.left_val>0,right_val<0，最大路径就是A.val+left_val
3.left_val<0,right_val>0，最大路径就是A.val+right_val
4.left_val>0,right_val>0，最大路径就是A.val+max(left_val+right_val)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=-sys.maxsize
        self.dfs(root)
        return self.res
    def dfs(self,root):
        if not root:
            return 0
        # 左子树的最大路径
        left_val=self.dfs(root.left)
        # 右子树的最大路径
        right_val=self.dfs(root.right)
        # 以root为最高点的最长路径长度，并和原来的最大值比较
        self.res=max(self.res,max(left_val,0)+max(right_val,0)+root.val)
        # 返回以root为起点的最长路径长度
        return max(left_val+root.val,right_val+root.val,root.val)

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(-2)
s=Solution()
print(s.maxPathSum(root))