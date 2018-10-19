'''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度
思路：找出二叉树左子树和右子数深度的最大值
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left_depth=self.TreeDepth(pRoot.left)
        right_depth=self.TreeDepth(pRoot.right)
        return max(left_depth,right_depth)+1


#非递归方法，层次遍历到最后一层，自然是最大深度，
class Solution2:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        stack=[pRoot]
        depth=0
        while stack:
            lens=len(stack)
            depth+=1
            for i in range(lens):
                tmp=stack.pop(0)
                if tmp.left:
                    stack.append(tmp.left)
                if tmp.right:
                    stack.append(tmp.right)
        return depth
