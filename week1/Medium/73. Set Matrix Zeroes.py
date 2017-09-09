"""
要尽量减少内存的使用 想法是除去第0行第0列的值外,全部遍历,若有matrix[i][j] = 0
则将对应matrix[i][0],matrix[0][j]设为0,这样只需要再下次遍历时 遇到首行首列中有0
就将对应的元素设为0,但是这个会影响到0行0列本身的判断,所以用两个标记,row,col如果0行0列中
原本就存在0则将对应值设为1,最后再判断row,col不为0的话,就将对应0行或者0列设为0
原地修改 空间O(1)
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        row,col = 0,0
        for i in range(m):
            if matrix[i][0] == 0:
                col = 1
                break
        for i in range(n):
            if matrix[0][i] == 0:
                row = 1
                break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0]==0:
                    matrix[i][j] = 0
        if row:
            for i in range(n):
                matrix[0][i] = 0
        if col:
            for i in range(m):
                matrix[i][0] = 0
        