"""
后序遍历的非递归实现,由于是先访问左子树,再访问右子树,最后才访问根节点,
要判断上一个访问的节点是左子树节点还是右子树节点决定是否访问根节点,用一个pre表示上一个访问的节点
如果当前节点的右子树为空或者pre等于其右子树节点,则访问其,否则,转到其右子树先访问其右子树

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        st,res = [],[]
        cur,lastVis = root,None
        while cur:
            st.append(cur)
            cur = cur.left
        while st:
            cur = st.pop()
            if cur.right == None or cur.right == lastVis:
                res.append(cur.val)
                lastVis = cur
            else:
                st.append(cur)
                cur = cur.right
                while cur:
                    st.append(cur)
                    cur=cur.left
        return res