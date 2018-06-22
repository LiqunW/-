'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
题意：合并两个已排序链表
思路：链表基本操作，双指针，每次比较，把较小的节点加入新链表。当一个链表为空，把剩下的链表全都加入新链表
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        new=ListNode(0)
        new_start=new
        p1=l1;p2=l2
        while l1 and l2:
            if l1.val < l2.val:
                new.next=l1
                l1=l1.next
            else:
                new.next=l2
                l2=l2.next
            new=new.next
        new.next=l1 or l2
        return new_start.next