'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
题意：判断链表的交汇处
思路：1先统计两个链表的长度，然后长的链表向后移动n，再判断
2.按照环路的思想，a，b指针同时出发，到头后从另一个链表的头部出发，如果存在交叉，必然会相遇
因为两个指针走过的路程是一样的，如果没有交叉，必然是都指向None节点
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA=headA;pB=headB
        while pA!=pB:
            pA=pA.next
            pB=pB.next
            if pA==pB:
                return pA
            if not pA:
                pA=headB
            if not pB:
                pB=headA
        return pA