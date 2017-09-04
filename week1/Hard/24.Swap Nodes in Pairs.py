"""
链表的题一般先考虑加个dummy结点之后 会比较轻松,这题用了三个
指针,pre,cur是每次交换的两个结点,交换完成之后继续将三个指针前移
交换其他结点
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        work = dummy
        pre = dummy.next
        cur = pre.next
        while cur:
            work.next = cur
            pre.next = cur.next
            cur.next = pre
            work = pre
            pre = pre.next
            
            cur = pre.next if pre else None
        return dummy.next
            