"""
矩阵元素从左至右从上到下依次递增,所以可以二分查找整个矩阵来做
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m,n = len(matrix),len(matrix[0])
        l,r = 0 , m*n-1
        while l <= r:
            mid = (l+r)>>1
            i,j = mid/n,mid%n
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False