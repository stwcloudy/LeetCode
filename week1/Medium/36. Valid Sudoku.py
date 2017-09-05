"""
这题比较简单,关键在于找到九宫格编号与行列号的关系
id = i/3*3+j/3
然后就用三个二维数组分别代表各自行,列,九宫格内出现的数字
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col = [[False]*10 for _ in range(9)]
        row = [[False]*10 for _ in range(9)]
        mat = [[False]*10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    if row[i][val] or col[j][val] or mat[i/3*3+j/3][val]:
                        return False
                    row[i][val] = True
                    col[j][val] = True
                    mat[i/3*3+j/3][val] = True
        return True
        