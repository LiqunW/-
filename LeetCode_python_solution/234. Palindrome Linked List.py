'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
题意：回文链表判断
思路：链表转数组，判断，时间空间复杂度O(N) 改进：只入栈一半，空间O(N/2)，其实还是O(N)
O(1)空间复杂度，后半部分链表翻转

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        slow = self.reverse(slow)
        tmp = head
        while slow:
            if tmp.val != slow.val:
                return False
            slow = slow.next
            tmp = tmp.next
        return True

    def reverse(self, node):
        new_head = None
        while node:
            p = node
            node = node.next
            p.next = new_head
            new_head = p
        return new_head