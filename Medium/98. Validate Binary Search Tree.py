"""
思路:
二叉排序树中序遍历之后是一个升序排列的数组
按照递归和非递归两种方法写
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder_trav(root):
            if root == None:
                return True
            if inorder_trav(root.left) == False:
                return False
            if self.prev != None and self.prev.val >= root.val:
                return False
            self.prev = root
            return inorder_trav(root.right)
        return inorder_trav(root)

class Solution(object):
    prev = None
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        prev = None
        vis = root
        st = []
        while st or vis:
            while vis:
                st.append(vis)
                vis = vis.left
            if st:
                x = st.pop()
                if prev != None and prev.val >= x.val:
                    return False
                prev = x
                vis = x.right
        return True