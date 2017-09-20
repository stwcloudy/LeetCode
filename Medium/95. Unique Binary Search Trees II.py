"""
和96题一样是利用i为根节点时,分别递归产生左右子树
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def generateBST(s,e):
            if s > e:
                return [None]
            tr = []
            for i in range(s,e+1):
                lsub_tree = generateBST(s,i-1)
                rsub_tree = generateBST(i+1,e)
                for l in lsub_tree:
                    for r in rsub_tree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        tr.append(root)
            return tr
        return generateBST(1,n)