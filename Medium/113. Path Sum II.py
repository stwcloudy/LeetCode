"""
思路:
这题是131题的扩展,需要输出路径上的数字,还是一样的采用递归的思想
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(root,sum,path,res):
            if not root:
                return 
            if not root.left and not root.right:
                if root.val == sum:
                    path.append(root.val)
                    res.append(path)
            if root.left:
                helper(root.left,sum-root.val,path+[root.val],res)
            if root.right:
                helper(root.right,sum-root.val,path+[root.val],res)
        helper(root,sum,[],res)
        return res