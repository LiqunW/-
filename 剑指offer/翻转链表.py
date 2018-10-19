'''
题意：输入一个链表，反转链表后输出新链表的表头
思路：同后往前建立链表，每次连接两个节点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        nHead=None
        while pHead:
            tmp=pHead
            pHead=pHead.next
            tmp.next=nHead
            nHead=tmp
        return nHead