"""
按照要求,采用了归并排序
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        def merge(h1,h2):
            dummy = ListNode(-1)
            cur = dummy
            while h1 and h2:
                if h1.val < h2.val:
                    cur.next = h1
                    h1 = h1.next
                else:
                    cur.next = h2
                    h2 = h2.next
                cur = cur.next
            if h1:
                cur.next = h1
            if h2:
                cur.next = h2
            return dummy.next
        def sort(head):
            if head.next == None:
                return head
            slow,fast = head,head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            nex = slow.next
            slow.next = None
            part1 = sort(head)
            part2 = sort(nex)
            nhead = merge(part1,part2)
            return nhead
        return sort(head)