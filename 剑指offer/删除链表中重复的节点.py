'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
思路：由于原表头可能是重复节点会被删除，因此，新建一个表头
'''



# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        dHead=ListNode(0)
        dHead.next=pHead
        prev=dHead # prev始终指向最后一个不重复的节点
        tmp2=pHead
        while tmp2 and tmp2.next:
            if tmp2.val==tmp2.next.val: # 判断条件是prev后的两个节点是否相等，若果相等的话，都要删除
                val_del=tmp2.val
                while tmp2 and (tmp2.val==val_del):
                    tmp2=tmp2.next
                prev.next=tmp2
            else:  # 不相等，就都向后移动一步
                prev=prev.next
                tmp2=tmp2.next
        return dHead.next