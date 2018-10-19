'''

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
思路：中序遍历，用pre存储上一个节点，left指向当前节点的前一个节点，right指向当前节点的后一个节点。
每次在递归遍历的时候设置一个pre，记录中序遍历时当前节点的前节点，然后将当前节点的左指针指向pre节点，
然后如果pre节点不为空则将pre的右节点指向当前节点，由此就形成了一个双向链表的前后指针。每次递归重复这两步，则可以形成一个完整的双向链表。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        pre = [None]
        root = self.helper(pRootOfTree, pre)
        # 树改造完后，root指向的是最后一个节点，因此用left回到头
        while root.left:
            root = root.left
        return root

    def helper(self, root, pre):
        if not root:
            return None
        if root.left:
            self.helper(root.left, pre)
        # pre 保存的是root节点的上一个节点
        root.left = pre[0]
        # 将上一个节点的right指向当前节点
        if pre[0]:
            pre[0].right = root
        #每次存储上一个节点
        pre[0] = root
        if root.right:
            self.helper(root.right, pre)
        return root

a=Solution()
root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)
a.Convert(root)