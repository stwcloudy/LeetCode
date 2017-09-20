"""
思路:
正常的中序遍历BST之后得到的是一个升序的序列,这题存在两个结点顺序交换了,那中序
得到的序列就不是升序,所以可以按照中序递归遍历该树,用prev指向遍历的上一个结点,
当碰到第一个逆序时,此时first为None,将其指向prev,second指向当前的root结点(注意此时第一个错误结点已经确定,不会再更改)
如果碰到第二个逆序(若存在的话)则second继续更新为当前的遍历root结点
最后将得到的两个结点的值交换即可

解法二:
不管是用递归还是自定义栈来做,空间复杂度都是O(n),要实现真正的O(1)的复杂度,需要使用线索二叉树
http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
用一种叫Morris traversal的方法
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first,self.second = None,None
        def trav_inorder(root):
            if root.left:
                trav_inorder(root.left)
            if self.prev and not self.first and self.prev.val >= root.val:
                self.first = self.prev
            if self.prev and self.first and self.prev.val >= root.val:
                self.second = root
            self.prev = root
            if root.right:
                trav_inorder(root.right)
        trav_inorder(root)
        self.first.val,self.second.val = self.second.val,self.first.val

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev,first,second = None,None,None
        cur = root
        while cur:
            if cur.left:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    if prev and prev.val > cur.val:
                        if not first:
                            first = prev
                        second = cur
                    prev = cur
                    tmp.right = None
                    cur = cur.right
            else:
                if prev and prev.val > cur.val:
                    if not first:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right
        if first and second:
            first.val,second.val = second.val,first.val