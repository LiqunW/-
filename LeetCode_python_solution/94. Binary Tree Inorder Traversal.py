'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

题意：二叉树中序遍历
思路：递归，迭代（）
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res=[]
        self.inorder(root)
        return self.res
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)


#非递归写法

class Solution2:
    def inorderTraversal(self,root):
        res=[]
        self.iterative_inorder(root,res)
        return res

    def iterative_inorder(self,root,res):
        stack=[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res