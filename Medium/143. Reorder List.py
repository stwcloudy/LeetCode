# Definition for singly-linked list.
"""
题意是将原链表L0->L1->L2->..->Ln变为L0->Ln->L1->Ln-1->...->
观察结果链表中的元素我发现:
除头节点之外的其余节点分为两个数量相等的部分,一个部分是以尾节点为起始节点逆序的链表
另一部分是以原链表第二个节点为起点顺序的节点,将这两个部分合并到头节点之后即为最终结果.
举个例子1,2,3,4,5,6,7
链表中间节点为4,两个部分分别为7,6,5 -- 2,3,4
最终结果为1,7,2,6,3,5,4
所以分为三个步骤求:
1.找到中间节点,将原链表划分为两个部分
2.将中间节点之后的部分逆序
3.合并两个部分链表
"""

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitList(self,head):
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head,mid
    def reverseList(self,head):
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy.next
        while cur.next:
            post = cur.next
            cur.next = post.next
            post.next = dummy.next
            dummy.next = post
        return dummy.next
    def mergeList(self,head1,head2):
        cur1 = head1
        head1 = head1.next
        while head1 or head2:
            if head2:
                cur1.next = head2
                cur1 = cur1.next
                head2 = head2.next
            if head1:
                cur1.next = head1
                cur1 = cur1.next
                head1 = head1.next
        return cur1
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        part1,part2 = self.splitList(head)
        part2 = self.reverseList(part2)
        head = self.mergeList(part1,part2)