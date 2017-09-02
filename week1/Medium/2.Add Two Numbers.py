# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
# 

"""
思路：
模拟高精度加法,创建一个结果头结点(虚拟),若最后一位进位大于0,则新添加一个ListNode在尾部即可
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0) #虚拟头结点
        cur = dummy
        carry = 0
        while l1 or l2:
        	val1 ,val2 = 0,0 #若其中一个链表已为空，自动赋值为0
        	if l1:
        		val1 = l1.val
        		l1 = l1.next
        	if l2:
        		val2 = l2.val
        		l2 = l2.next
        	digit = val1 + val2 + carry
        	cur.next = ListNode(digit%10)
        	cur = cur.next
        	carry = digit/10
	    if carry != 0:
	    	cur.next = ListNode(carry)
	    	cur = cur.next
	    return dummy.next
