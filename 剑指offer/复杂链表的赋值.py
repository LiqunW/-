'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
思路：1.复制原链表的每个节点，复制random节点，拆分链表，注意不要使用pHead，用一个新的引用来代替
'''

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None: return None
        tmp = pHead
        while tmp:
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next
        tmp = pHead
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        newhead = pHead.next
        pold = pHead
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead