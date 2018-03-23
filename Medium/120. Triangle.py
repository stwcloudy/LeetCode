"""
简单的动态规划的题,但是有一个小技巧是基于数据的特殊形式
自下而上的计算更好
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        dp = [0]*(m+1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i],dp[i+1])
        return dp[0]