'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路：二叉树中序遍历是左根右，因此先判断该节点是否为空，如果为空，则直接返回
如果该节点有右子节点，则从该右子节点开始，找到，该节点的最左子节点
如果没有右子节点，则向上找父节点，一直找到父节点的子节点等于该节点为止，没有返回空

1.二叉树为空，则返回空；
2.节点右孩子存在，则设置一个指针从该节点的右孩子出发，一直沿着指向左子结点的指针找到的叶子节点即为下一个节点；
3.节点不是根节点。如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        while pNode.next:
            if pNode.next.left==pNode:
                return pNode.next
            else:
                pNode=pNode.next
        return