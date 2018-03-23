"""
这题承接116,不同的是二叉树不是完全二叉树,且要求常数空间,一开始想的是还是
按照116题的思路做，但是判断语句太多,后来才发现可以用一个虚拟头节点表示下层的第一个节点,这样就不用判断很多情况
循环时,只需要让pre指向dummy.next即可
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        pre = root
        dummy = TreeLinkNode(-1)
        cur = dummy
        while pre:
            cur.next = pre.left
            if cur.next:
                cur = cur.next
            cur.next = pre.right
            if cur.next:
                cur = cur.next
            pre = pre.next
            if not pre:
                pre = dummy.next
                cur = dummy