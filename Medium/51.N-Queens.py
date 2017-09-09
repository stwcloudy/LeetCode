"""
解法一:
遍历每一行可以放皇后的位置,生成一个方案放入结果中,
r[i]=j表示第i行第j列放皇后
判断时 皇后不能同列和对角线
解法二:

"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isvalid(row,col):
            for i in range(row):
                if col == r[i] or abs(col - r[i]) == abs(row-i):
                    return False
            return True
        def dfs(row,res):
            if row == n:
                sol = []
                for i in range(n):
                    q = ['.']*n
                    q[r[i]] = 'Q'
                    sol.append(''.join(q))
                res.append(sol)
                return
            for j in range(n):
                r[row] = j
                if isvalid(row,j):
                    dfs(row+1,res)
        r = [0]*n
        res = []
        dfs(0,res)
        return res