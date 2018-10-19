'''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，(5，3，7，2，4，6，8）中，
按结点数值大小顺序第三小结点的值为4。

思路：中序遍历，用一个cnt记录当前节点是第几个节点，等于k的时候就是第k小的节点
'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k<=0:
            return
        self.res = None
        self.cnt=0
        self.inorder(pRoot,k)
        return self.res
    def inorder(self,pRoot,k):
        if not pRoot:
            return
        self.inorder(pRoot.left,k)
        self.cnt+=1
        if k==self.cnt:
            self.res = pRoot
            return
        self.inorder(pRoot.right,k)
        return