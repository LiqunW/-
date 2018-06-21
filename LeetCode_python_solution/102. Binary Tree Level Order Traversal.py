'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
题意：按层输出二叉树
思路：BFS，利用队列完成即可
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        level=[]
        level.append(root)
        while len(level):
            res.append([node.val for node in level])
            next_level = []
            for item in level:
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)
            level = next_level
        return res