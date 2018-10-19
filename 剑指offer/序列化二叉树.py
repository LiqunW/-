'''
请实现两个函数，分别用来序列化和反序列化二叉树
序列化可以基于先序/中序/后序/按层等遍历方式进行，这里采用先序遍历的方式实现，字符串之间用 “，”隔开。
反序列化二叉树：根据某种遍历顺序得到的序列化字符串，重构二叉树。具体思路是按前序遍历“根左右”的顺序，
根节点位于其左右子节点的前面，即非空（#）的第一个节点是某子树的根节点，左右子节点在该根节点后，以空节点#为分隔符。
'''




# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val)+','+self.Serialize(root.left)+','+self.Serialize(root.right)
    def Deserialize(self, s):
        # write code here
        s_list=s.split(',')
        return self.deserializeTree(s_list)
    def deserializeTree(self,s_list):
        if len(s_list)<=0:
            return None
        val = s_list.pop(0)
        root=None
        if val!='#':
            root=TreeNode(int(val))
            root.left=self.deserializeTree(s_list)
            root.right=self.deserializeTree(s_list)
        return root