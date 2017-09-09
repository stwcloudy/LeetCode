"""
还是添加一个头结点,再用两个指针指向要翻转的链表的前一个结点和最后一个结点
(初始时,start = dummy,end = 不算dummy的第k个结点)
然后调用链表翻转的函数,对其进行操作,返回翻转后的最后一个字符作为新的start结点
此处用的链表翻转的方法是使用两个指针,pre,cur,操作流程如下
{
    此处所写代码是针对整个单链表翻转的,与题中代码略有差异:
    dummy.next = head
    pre = dummy.next
    while pre.next:
        #每次完成一个元素的翻转
        cur = pre.next
        pre.next = cur.next #先将后续的结点串起来
        cur.next = dummy.next # 此处cur的next域指向的始终是dummy.next,即首个结点
        dummy.next = cur

}
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        start,end = dummy,dummy
        i = 0
        def helper(start,end):
            pre = start.next
            tmp = start.next
            print tmp.val
            cur = None
            while cur != end:
                cur = pre.next
                pre.next = cur.next
                cur.next = start.next
                start.next = cur
            return (tmp,tmp)
        while end and i < k:
            end = end.next
            i += 1
            if i == k:
                start,end = helper(start,end)
                i = 0
        return dummy.next