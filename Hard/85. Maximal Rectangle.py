"""
思路:
与84题一样,只不过转化为了二维中的计算,每次以第i行为底计算高度,这就把以每一行为
底转化为了84题,再求最大值即可
以下代码可以转化为一维数组 节省空间:
也可以采用之前动态规划求解的方法
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix[0]) == 0:
            return 0
        m,n = len(matrix),len(matrix[0])
        heights = [[0]*n for _ in range(m)]
        for j in range(n):
            heights[0][j] = int(matrix[0][j])
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j] != '0':
                    heights[i][j] = int(matrix[i][j]) + heights[i-1][j]
        res = 0
        def helper(arr):
            st = []
            area = 0
            arr.insert(0,0)
            arr.append(0)
            st.append(0)
            for i in range(1,len(arr)):
                while arr[i] < arr[st[-1]]:
                    idx = st[-1]
                    st.pop()
                    area = max(area,arr[idx]*(i-(st[-1]+1)))
                st.append(i)
            return area
        for i in range(m):
            res = max(res,helper(heights[i][:]))
        return res

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n,m = len(matrix),len(matrix[0])
        heights = [0]*(m+1)
        res = 0
        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for j in range(len(heights)):
                while heights[j] < heights[stack[-1]]:
                    idx = stack.pop()
                    res = max(res,heights[idx]*(j - stack[-1] - 1))
                stack.append(j)
        return res

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n,m = len(matrix),len(matrix[0])
        print n,m
        left,right = [0]*m,[0]*m
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
        for i in range(1,n):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        print matrix
        res = 0
        for i in range(0,n):
            for j in range(m):
                left[j] = j
                while left[j] > 0 and matrix[i][left[j]-1] >= matrix[i][j]:
                    left[j] = left[left[j] - 1]
            for j in range(m-1,-1,-1):
                right[j] = j
                while right[j] < m-1 and matrix[i][right[j] + 1] >= matrix[i][j]:
                    right[j] = right[right[j] + 1]
            for j in range(m):
                res = max(res,matrix[i][j]*(right[j] - left[j] + 1))
        return res