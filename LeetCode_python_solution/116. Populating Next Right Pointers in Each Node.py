'''
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL

题意：按要求把二叉树变成链表
思路：由于是完全二叉树，所以若节点的左子结点存在的话，其右子节点必定存在，
所以左子结点的next指针可以直接指向其右子节点，对于其右子节点的处理方法是，判断其父节点的next是否为空，
若不为空，则指向其next指针指向的节点的左子结点，若为空则指向NULL
也可以用bfs做，因为只能使用O(1)的空间，所以用两个指针完成操作
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root and root.left:
            root.left.next=root.right
            if root.next:
                root.right.next=root.next.left
            else:
                root.right.next=None
            self.connect(root.left)
            self.connect(root.right)
# 用两个指针prev和curr，其中prev标记每一层的起始节点，curr用来遍历该层的节点
class Solution2:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        prev, curr = root, None
        while prev.left:
            curr = prev
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                else:
                    curr.right.next = None
                curr = curr.next
            prev = prev.left