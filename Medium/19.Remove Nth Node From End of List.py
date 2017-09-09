"""
思路:删除倒数第n个结点,因为存在特殊情况删除链表的第一个结点,所以生成一个fake的头结点
这样就不用特殊处理,用两个指针slow,fast,先将fast向前移n个位置,然后两个指针同时移动,直至fast.next
为空,此时slow.next即为要删除的结点
(这个题由于题目中明确说明所给n一定合法,所以不用对n做情况判断)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        slow,fast = dummy,dummy
        while n:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next