"""
往四个方向上的dfs,可以写四个dfs调用
我这里采用的是将其方向存在两个数组中 dx,dy 采用for循环遍历四个方向上的合法位置
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        m,n = len(board),len(board[0])
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        def dfs(x,y,index):
            if index == len(word):
                return True
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if xx >= 0 and xx < m and yy >= 0 and yy < n and board[xx][yy] == word[index]:
                    tmp = board[xx][yy]
                    board[xx][yy] = '#'
                    if dfs(xx,yy,index+1):
                        return True
                    board[xx][yy] = tmp
            return False
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = '#'
                    if dfs(i,j,1):
                        return True
                    board[i][j] = tmp
        return False