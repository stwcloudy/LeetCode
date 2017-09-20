# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder and not inorder:
            return None
        root = TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:pos],postorder[:pos])
        root.right = self.buildTree(inorder[pos+1:],postorder[pos - len(postorder):-1])
        return root

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder and not inorder:
            return None
        def helper(start,end):
            if start <= end:
                root = TreeNode(postorder.pop())
                i = inorder.index(root.val)
                root.right = helper(i+1,end)
                root.left = helper(start,i-1)
                return root  
                
        return helper(0,len(inorder)-1)