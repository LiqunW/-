'''
操作给定的二叉树，将其变换为源二叉树的镜像。
思路：递归交换root节点的左右子节点即可
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        if root.left:
            root.left=self.Mirror(root.left)
        if root.right:
            root.right=self.Mirror(root.right)
        root.left,root.right=root.right,root.left
        return root