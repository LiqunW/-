'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
题意：二叉树打印，偶数行翻转
思路：bfs，设置一个flag隔行翻转数组即可
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        level=[root]
        zig_flag=False
        while level:
            if zig_flag:
                res.append([i.val for i in level[::-1]])
            else:
                res.append([i.val for i in level])
            next_level=[]
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level=next_level
            zig_flag=~zig_flag
        return res