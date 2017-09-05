"""
与求合法数独状态一样,用三个二维数组存储行,列,小九宫格的数字存在情况
递归回溯求解

"""
class Solution(object):
    def dfs(self,board,no):
        i,j = no/9,no%9
        if no == 81:
            return True
        if board[i][j] == '.':
            for x in range(1,10):
                if not self.row[i][x] and not self.col[j][x] and not self.mat[i/3*3+j/3][x]:
                    self.row[i][x] = True
                    self.col[j][x] = True
                    self.mat[i/3*3+j/3][x] = True
                    board[i][j] =  str(x)
                    if self.dfs(board,no+1):
                        return True
                    board[i][j] = '.'
                    self.row[i][x] = False
                    self.col[j][x] = False
                    self.mat[i/3*3+j/3][x] = False
        else:
            if self.dfs(board,no+1):
                return True
        return False
    def solveSudoku(self, board):
        
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.col = [[False]*10 for _ in range(9)]
        self.row = [[False]*10 for _ in range(9)]
        self.mat = [[False]*10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    self.row[i][val] = True
                    self.col[j][val] = True
                    self.mat[i/3*3+j/3][val] = True
        self.dfs(board,0)