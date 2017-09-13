"""
解法一:
要求转化的BST是要求平衡的,所以每次的根是当前的链表的中间节点的值
用两个指针,slow,fast,当fast.next.next还未到tail的时候,slow向前移一个结点,fast移两个
这样停下来的位置slow刚好指向根节点的值 再递归构造左子树和右子树

解法二:
不同的地方在于先将链表中的元素存在列表中,再按下标读取中间元素的值构造根
递归构造左子树右子树
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        def toBST(head,tail):
            if head == tail:
                return None
            slow,fast = head,head
            while fast.next != tail and fast.next.next != tail:
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            root.left = toBST(head,slow)
            root.right = toBST(slow.next,tail)
            return root
        return toBST(head,None)

class Solution(object):
    def BST(self,nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[-1])
        l,r = 0,len(nums) - 1
        mid = (l+r)>>1
        root = TreeNode(nums[mid])
        root.left = self.BST(nums[:mid])
        root.right = self.BST(nums[mid+1:])
        return root
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        nums = []
        tail = head
        while tail:
            nums.append(tail.val)
            tail = tail.next
        print nums
        return self.BST(nums)