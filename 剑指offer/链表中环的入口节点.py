'''
链表中环的入口节点
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路：快慢指针的思路，slow指针一次走一步，fast一次走两步，如果相遇说明环路存在
然后让slow指针从头开始走，fast指针每次走一步，两个指针相遇的地方就是环的入口
'''


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return
        slow=pHead
        fast=pHead
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        slow=pHead
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return fast