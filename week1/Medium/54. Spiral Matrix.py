"""
模拟右下左上即可
分别用left,right,top,bottom表示左右上下边界
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m,n = len(matrix),len(matrix[0])
        res = []
        left,right,bottom,top = 0,n-1,m-1,0
        print left,right,bottom,top
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
            bottom -= 1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
            left += 1
        return res
                