"""
删除所有重复元素,slow指向最后一个不重复的结点,找到下一个不重复的元素
slow.next指向它,否则fast指针前移
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        slow,fast = dummy,dummy.next
        while fast:
            while fast.next and slow.next.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow = slow.next
            else:
                slow.next = fast.next
            fast = fast.next
        return dummy.next