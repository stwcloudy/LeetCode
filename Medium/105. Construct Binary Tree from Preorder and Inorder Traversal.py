"""
思路:
利用前序和中序遍历来还原二叉树,可以利用前序遍历的首元素一定是根元素
然后在中序遍历中找到根元素值所在位置,则其之前的数都为左子树
之后的数都为右子树,分别递归构造即可
和106用后序中序遍历二叉树思路一样
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+pos],inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:],inorder[pos+1:])
        return root