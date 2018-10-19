'''
题意：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
思路：归并排序，如果两个链表长度不一致，当其中一个链表为空时，把另一个链表剩下的部分直接加到新链表中
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        nHead=ListNode(0)
        new=nHead
        while pHead1 and pHead2:
            if pHead1.val>pHead2.val:
                new.next=pHead2
                pHead2=pHead2.next
            else:
                new.next=pHead1
                pHead1=pHead1.next
            new=new.next
        if pHead1:
            new.next=pHead1
        if pHead2:
            new.next=pHead2
        return nHead.next