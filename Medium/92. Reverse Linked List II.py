"""
思路:
类似与全部链表反转的题,为了处理头结点翻转,加入一个虚头结点
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        diff = n - m
        m -= 1
        while m:
            pre = pre.next ##翻转前的结点
            m -= 1
        print diff
        cur = pre.next
        for i in range(diff):
            if cur.next:
                post = cur.next
                cur.next = post.next
                post.next = pre.next
                pre.next = post
        return dummy.next
        