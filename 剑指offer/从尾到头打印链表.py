'思路：链表从前往后遍历，用一个队列保存节点，每次得到的节点从头部入队'

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        res=[]
        while listNode:
            res.insert(0,listNode.val)
            listNode=listNode.next
        return res