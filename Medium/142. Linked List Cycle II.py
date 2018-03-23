"""
本题思路分几个步骤进行,此题的要求是如果链表中存在环则返回环的起始节点,所以分为几个步骤:
1.要先判断是否存在环
这个步骤的要求即是141题的原题,要判断是否存在环,只需要用两个指针,一个走的快往前走两步,一个走
得慢只走一步,这样的话,如果链表中存在环,则两个指针一定会相遇,所以相遇时即表示存在环,否则无环
2.寻找环的入口
我们知道在寻找单链表的倒数第K个节点时,采用的是先将快指针往前移动k步,之后两个指针一起移动,这样由于
快慢指针距离始终为k,当fast指针到达为空(链表末尾之后)时,slow指向的刚好就是倒数第k个节点
受其启发,如果我们知道环中的节点数,假设为k,先将fast指针向前移动k个位置,slow,fast再同时移动,如果
不考虑环,当fast到达最后一个节点,两个节点再移动一次即为所找节点,由于环的存在,fast再往前移动一步回到环的起始节点
而slow也是,所以判断条件是slow==fast
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        def existCircle(head):
            if not head:
                return None
            slow,fast = head,head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return fast
            return None
        meeting = existCircle(head)
        if meeting == None:
            return None
        numloop = 1
        work = meeting
        while work.next != meeting:
            work = work.next
            numloop += 1
        slow,fast = head,head
        for _ in range(numloop):
            fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow