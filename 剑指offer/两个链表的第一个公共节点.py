'''

输入两个链表，找出它们的第一个公共结点。
思路：两个指针分别指向两个链表，当一个指针走到头后，指向另一个链表的头，继续走，直到两个指针相遇或者都走到头

'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        p,q=pHead1,pHead2
        while p and q and p!=q:
            p=p.next
            q=q.next
            if p==q:
                return p
            elif not p:
                p=pHead2
            elif not q:
                q=pHead1
        return p