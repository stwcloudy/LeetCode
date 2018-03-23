"""
思路:
由于在边界上的'O'不用变化,则可以寻找每个边界位置为'O'的地方,进行dfs或者bfs
将找到的'O'也一样标记为'*',最后在改变之后的board中依旧为'O'的改为'X',其余'*'
还原成'O' 用python dfs会超时
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        if len(board) <=2 or len(board[0]) <= 2:
            return
        m,n = len(board),len(board[0])
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        def bfs(x,y):
            q.append((x,y))
            board[x][y] = '*'
            while q:
                i,j = q.pop(0)
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if xx>=0 and xx < m and yy>=0 and yy < n and board[xx][yy] == 'O':
                        q.append((xx,yy))
                        board[xx][yy] = '*'
                    
            return
        q = []
        for i in range(m):
            if board[i][0] == 'O':
                bfs(i,0)
            if board[i][n-1] == 'O':
                bfs(i,n-1)
        for i in range(n):
            if board[0][i] == 'O':
                bfs(0,i)
            if board[m-1][i] == 'O':
                bfs(m-1,i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                
            