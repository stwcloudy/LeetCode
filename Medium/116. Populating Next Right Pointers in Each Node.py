"""
思路:
法一:
普通的O(n)的空间,层次遍历,将每层的结点以next域连接起来
法二:
该方法有效的利用了next指针,每次保证从该层的最左节点开始,以上层节点的right节点作为当前节点的next域
保证上层节点和该层节点共同移动

"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        st = [root]
        while st:
            level = len(st)
            for i in range(level):
                node = st[0]
                if i == level - 1:
                    node.next = None
                else:
                    node.next = st[1]
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
                st.pop(0)
            
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        pre,cur = None,root
        while cur:
            tmp = cur
            while pre and cur:
                cur.next = pre.right
                cur = cur.next
                pre = pre.next
                if pre:
                    cur.next = pre.left
                    cur = cur.next
                else:
                    break
            pre = tmp
            cur = tmp.left