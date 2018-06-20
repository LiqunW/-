'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
题意：输出bst中的第k小元素
思路：中序遍历，递归或者非递归都可以
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if k==1:
                return root.val
            else:
                k-=1
                root=root.right


class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = None
        self.k = k
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        if root.left:
            self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
        if root.right:
            self.helper(root.right)