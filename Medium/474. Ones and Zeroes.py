"""
思路:
一开始我想的太简单,以为贪心的选择最短的字符就是最多的答案,可是现有0,1的个数不均衡的情况下这样做得不到最优解
比如:
"111 1000 1000 1000" 9,3 如果按照贪心选择 答案为1但实际答案是3
所以后来转换思路之后发现这就是一个二维(限制在两个方向上)的0-1背包,所以按照0-1背包求解即可
"""

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(m+1)]
        def find(tmp):
            zero,one = 0,0
            for ch in tmp:
                if ch == '1':
                    one += 1
                else:
                    zero += 1
            return (zero,one)
        for i in range(len(strs)):
            zero,one = find(strs[i])
            for j in range(m,zero-1,-1):
                for k in range(n,one-1,-1):
                    dp[j][k] = max(dp[j][k],dp[j-zero][k-one]+1)
        return dp[m][n]