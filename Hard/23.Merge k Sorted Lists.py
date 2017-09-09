"""
思路：
采取二路归并的思想,分治。
需要注意的地方在于基础情况:
1.lists为空 返回None
2.只有一个链表,直接返回该链表
3.即便有多个链表,其中有的链表也可能为空,在merge2Lists函数中判断
我这做了个小优化长度为2的时候也是直接调用merge2Lists,而不经过helper函数分治(python的情况下快额70ms左右)

法二:
还有一种方法是利用最小堆或者是库中的优先队列(python中优先队列实际就是用最小堆实现)
先将每个链表头结点入队,生成一个虚拟头结点先指向第一个出队的结点,并将该结点的next结点入队(如果存在)
这样每次出队之后得到的都是具有最小值的结点(该处是将(node.val,node)作为一个元组入队)
遍历完所有链表元素后,也得到了相应的结果

两种算法的时间复杂度都是sigma(ni)*log(k)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2Lists(l1,l2):
            if not l1 and not l2:
                return None
            if not l1:
                return l2
            if not l2:
                return l1
            head,cur = None,None
            while l1 and l2:
                if head == None:
                    if l1.val < l2.val:
                        head = cur = l1
                        l1 = l1.next
                    else:
                        head = cur = l2
                        l2 = l2.next
                    cur.next = None
                else:
                    if l1.val < l2.val:
                        cur.next = l1
                        l1 = l1.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                    cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return head
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return merge2Lists(lists[0],lists[1])
        def helper(l,r):
            if l == r:
                return lists[l]
            if l + 1 == r:
                return merge2Lists(lists[l],lists[r])
            mid = (l+r)>>1
            left = helper(l,mid)
            right = helper(mid+1,r)
            return merge2Lists(left,right)
        res = helper(0,len(lists)-1)
        return res

###Solution2
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        dummy = ListNode(-1)
        cur = dummy
        for node in lists:
            if node:
                heapq.heappush(h,(node.val,node))
        while h:
            cur.next = heapq.heappop(h)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(h,(cur.next.val,cur.next))
        return dummy.next