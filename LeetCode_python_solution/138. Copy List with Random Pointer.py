'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
题意：带有随机指针的链表复制
思路：1.复制给定链表中的每一个节点，将其插入到给定链表中原节点的后面。
2.复制random节点。由于新节点就在原节点的后面，因此，依次检测给定链表中的每个节点，
若random不为空，则将它的下一个节点（对应新节点）的random指针指向原节点random指针所指节点的下一个节点。
3.将链表拆分成新旧两个链表即可
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None: return None
        tmp = head
        while tmp:
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead