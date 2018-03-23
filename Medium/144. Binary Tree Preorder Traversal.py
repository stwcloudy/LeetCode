"""
用栈实现前序中序后序的遍历,模拟其访问顺序即可
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        st = []
        while root or st:
            while root:
                res.append(root.val)
                st.append(root)
                root = root.left
            root = st.pop()
            root = root.right
        return res
                