'''
两个相同大小的0,1方阵A,B 可以将A矩阵向上下左右滑动,求与B矩阵最大覆盖(相同位置为1)
朴素方法O(N^4)
解法：
1. 先将A,B矩阵中为1的位置记录下来；
2. 遍历记录下来的所有位置(ia,ja),(ib,jb)来说, 都可以通过上下左右的滑动从A到B,而所采取的移动方式即为(ia-ja),(ja-jb),
比如(3,2),(1,4)就表示横移和竖移的值为(2,-2)正负代表方向,所以将水平，竖直方向的移动以元组作为key,每出现一个加1,最后取字典中的最大值即可
'''
class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        la = [(i,j) for i in range(n) for j in range(n) if A[i][j] == 1]
        lb = [(i,j) for i in range(n) for j in range(n) if B[i][j] == 1]
        
        res = 0
        overlap = collections.defaultdict(int)
        for x in la:
            for y in lb:
                key = (x[0]-y[0],x[1]-y[1])
                overlap[key] += 1
                res = max(res, overlap[key])
        return res
                