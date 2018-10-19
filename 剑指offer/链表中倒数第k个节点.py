'''
输入一个链表，输出该链表中倒数第k个结点。
思路：fast指针先走k步数，然后slow指针从头开始走，当fast指向链表末尾时，slow指针指向倒数第k个节点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return head
        fast=head
        cnt=0
        while fast and cnt<k:
            fast=fast.next
            cnt+=1
        if cnt!=k:
            return
        slow=head
        while fast:
            slow=slow.next
            fast=fast.next
        return slow