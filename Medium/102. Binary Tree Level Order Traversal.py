"""
思路:
二叉树的层次遍历 用队列,单独输出每一层的数据
用psize,csize分别表示输出的当前层和下层的节点数目,psize为0时表示本层遍历完毕
加入结果
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = Queue.Queue()
        q.put(root)
        psize,csize = 1,0
        res = []
        tmp = []
        while not q.empty():
            node = q.get()
            tmp.append(node.val)
            if node.left:
                q.put(node.left)
                csize += 1
            if node.right:
                q.put(node.right)
                csize += 1
            psize -= 1
            if psize == 0:
                res.append(tmp)
                tmp = []
                psize = csize
                csize = 0
        return res

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        while q:
            tot = len(q)
            tmp = []
            for i in range(tot):
                node = q[0]
                tmp.append(node.val)
                q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)
        return res
            