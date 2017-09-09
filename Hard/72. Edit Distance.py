"""
思路:
动态规划,dp[i][j]表示从word1[0-i-1]->word2[0-j-1]的最小编辑距离
dp[i][j]= 
1.若最后一步是删除一个字符,则为dp[i][j-1] + 1
2.若最后一步是添加一个字符,则为dp[i-1][j] + 1
3.替换,如果word1[i-1] == word2[j-1]则dp[i][j] = dp[i-1][j-1]否则再加替换的那步的1
所以,dp[i][j] = min(dp[i-1][j] + 1,dp[i][j-1]+1,dp[i-1][j-1] + (1))的最小值
结果为dp[m][n]
时间复杂度为O(MN)
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        m,n = len(word1),len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j] + 1
                if dp[i][j-1] + 1 < dp[i][j]:
                    dp[i][j] = dp[i][j-1] + 1
                add = 1 if word1[i-1] != word2[j-1] else 0
                dp[i][j] = min(dp[i][j],dp[i-1][j-1] + add)
        return dp[m][n]
        