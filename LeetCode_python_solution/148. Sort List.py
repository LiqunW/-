'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
题意：链表排序，时间复杂度O(nlogn),空间复杂度O(1)
思路：归并排序，用快慢指针找到链表的中间节点，重建链表的时候要新建一个表头
由于链表在归并操作时并不需要像数组的归并操作那样分配一个临时数组空间，
所以这样就是常数空间复杂度了，当然这里不考虑递归所产生的系统调用的栈
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: #分到只剩一个节点为止
            return head
        mid = self.findmid(head)
        rhead = mid.next
        mid.next = None
        return self.merge(self.sortList(head), self.sortList(rhead))

    def merge(self, left, right):
        tmpNode = ListNode(0)
        newHead = tmpNode
        while left and right:
            if left.val < right.val:
                newHead.next = left
                left = left.next
            else:
                newHead.next = right
                right = right.next
            newHead = newHead.next
        if left:
            newHead.next = left
        if right:
            newHead.next = right
        return tmpNode.next

    def findmid(self, head): #快慢指针找中间节点
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow