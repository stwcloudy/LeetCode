"""
正确的括号匹配的数目是一个catlan数,递归构造合法解
"""

class Solution(object):
    def helper(self,n,m,match,res):
        if n == 0 and m == 0:
            res.append(match)
        if n > 0 :
            self.helper(n-1,m,match+'(',res)
        if m > 0 and n < m:
            self.helper(n,m-1,match+')',res)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0:
            return []
        self.helper(n,n,'',res)
        return res
        