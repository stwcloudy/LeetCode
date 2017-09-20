"""
这题承接下一题需要写出所有合法的BST,单独求个数的话,每次固定根节点为i,
此时的二叉树的个数为f[i-1]*f[n-i]
答案就是所有的f[i]的累加
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0]*(n+1)
        f[0] = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                f[i] += f[j-1]*f[i-j]
        return f[n]