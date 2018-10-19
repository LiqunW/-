'''
输入一颗二叉树，判断是否为平衡二叉树
思路：平衡二叉树是空数或者左右子树深度相差不大于1，并且它的子树也是平衡二叉树
方法1：递归求解深度即可
方法2：后序遍历二叉树，同时求子树高度，这样只需要遍历一遍即可
'''




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        d_left=self.getDepth(pRoot.left)
        d_right=self.getDepth(pRoot.right)
        if abs(d_left-d_right)>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def getDepth(self,root):
        if not root:
            return 0
        left=self.getDepth(root.left)
        right=self.getDepth(root.right)
        return max(left,right)+1


class Solution2:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        res=self.IsBalanced(pRoot)
        return res>=0
    def IsBalanced(self,pRoot):
        if not pRoot:
            return 0
        left=self.IsBalanced(pRoot.left)
        right=self.IsBalanced(pRoot.right)
        if abs(left-right)>1 or left==-1 or right==-1:
            return -1
        return max(left,right)+1