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
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
题意：给的是非满二叉树
思路：建立一个dummy结点来指向每层的首结点的前一个结点，然后指针node用来遍历这一层，我们实际上是遍历一层，然后连下一层的next，
首先从根结点开始，如果左子结点存在，那么node的next连上左子结点，然后node指向其next指针；如果root的右子结点存在，
那么node的next连上右子结点，然后node指向其next指针。此时root的左右子结点都连上了，此时root向右平移一位，
指向其next指针，如果此时root不存在了，说明当前层已经遍历完了，我们重置t为dummy结点，root此时为dummy->next，即下一层的首结点，
然后dummy的next指针清空
'''
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy=TreeLinkNode(-1)
        node=dummy
        while root:
            if root.left:
                node.next=root.left
                node=node.next
            if root.right:
                node.next=root.right
                node=node.next
            root=root.next
            if not root:
                node=dummy
                root=dummy.next
                dummy.next=None