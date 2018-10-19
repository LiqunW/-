'''
题意:二叉树的层次遍历
思路：用栈记录每层的节点，按次序打印即可
'''
#牛客显示空间复杂度过大，改进后可以不使用next_level这个辅助栈
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return root
        current=[root]
        next_level=[];res=[]
        while current:
            res.append([i.val for i in current])
            for i in current:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            current=next_level
        return res

#用一个变量记录当前level的长度
class Solution2:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        current=[root]
        res=[]
        while current:
            _len=len(current)
            for i in range(_len):
                node=current.pop(0)
                res.append(node.val)
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
        return res