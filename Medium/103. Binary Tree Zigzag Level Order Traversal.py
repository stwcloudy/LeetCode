"""
本题以zigzag型层次遍历二叉树,可用双向队列来做
顺序输出当前层的值时,从队列末尾读取节点,分别将节点的left,right节点加入队列前端
逆序输出当前层的值时,从队列前端读取节点,分别将节点的right,left节点加入队列后端

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        que,res = [],[]
        que.append(root)
        clock_wise = 1
        while que:
            q_sz = len(que)
            clock_wise ^= 1
            tmp = []
            for _ in range(q_sz):
                if clock_wise == 1:
                    nodes = que.pop(0)
                    tmp.append(nodes.val)
                    if nodes.right:
                        que.append(nodes.right)
                    if nodes.left:
                        que.append(nodes.left)
                else:
                    nodes = que.pop()
                    tmp.append(nodes.val)
                    if nodes.left:
                        que.insert(0,nodes.left)
                    if nodes.right:
                        que.insert(0,nodes.right)
            res.append(tmp)
        return res