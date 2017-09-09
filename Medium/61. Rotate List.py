"""
方法是先将链表首尾相连 再根据k值来进行移动指针,注意k有可能大于链表长度即可
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head :
            return head
        dummy = ListNode(-1)
        dummy.next = head
        n = 0
        work = head
        while work:
            n += 1
            work=work.next
        k = k % n
        if k == 0:
            return head
        fast = dummy
        while fast.next:
            fast = fast.next
        fast.next = dummy.next
        for _ in range(n-k):
            fast=fast.next
        dummy.next = fast.next
        fast.next = None
        return dummy.next