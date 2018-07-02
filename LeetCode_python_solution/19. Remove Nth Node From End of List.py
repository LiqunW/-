'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
题意：删除链表倒数第n个节点
思路：倒数第n个就是正数K-n个(K为链表长度)，因为是删除操作，需要指向待删除节点的前一个节点，
链表添加一个头，fast指针先走n+1步，然后slow指针从头开始走，直到fast指针指向链表尾，
slow指针指向倒数n+1个节点
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new=ListNode(-1)
        new.next=head
        fast=new
        for i in range(n+1):
            fast=fast.next
        slow=new
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return new.next