'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
题意：链表翻转
思路：倒序建立链表
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new=None
        while head:
            tmp=head
            head = head.next  #这行不能放在最后，因为tmp和head为同一链表的引用，tmp.next=new会影响head.next的值
            tmp.next=new
            new=tmp

        return new

a1=ListNode(1)
a2=ListNode(2)
a2.next=a1
a3=ListNode(3)
a3.next=a2
s=Solution()
new=s.reverseList(a3)
print(new.val)
print(new.next.val)
print(new.next.next.val)