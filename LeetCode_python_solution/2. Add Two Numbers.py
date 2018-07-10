'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
题意：链表加法
思路：按位相加即可，记录进位的情况
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sums = ListNode(0)
        head = sums
        carry = 0
        while l1 or l2 or carry:
            tmp = 0
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            if carry:
                tmp += carry
                carry = 0
            if tmp >= 10:
                tmp -= 10
                carry = 1
            head.next = ListNode(tmp)
            head = head.next
        return sums.next
