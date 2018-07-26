'''
We partition a row of numbers A into at most K adjacent (non-empty) groups, 
then our score is the sum of the average of each group. What is the largest score we can achieve?

solution:
动态规划,dp[i][k]表示到A[:i]划分为k个部分的最大结果,
则动态转移方程与dp[j][k-1]有关，其中j<k 且保证j>=k-1
dp[i][k] = max(dp[i][k],dp[j][k-1] + partsum(j,i)／(i-j))
其中partsum表示从A[j+1:i]的部分和

'''
class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        if not A:
            return 0
        if K == 1:
            return sum(A) / n
        if n <= K:
            return sum(A)
        partsum = [0]
        for num in A:
            partsum.append(partsum[-1] + num)
        dp = [[0]*(K+1) for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][1] = partsum[i] / i
        for k in range(2,K+1):
            for i in range(1,n+1):
                for j in range(1,i-k+2):
                    tmp = (partsum[i] - partsum[i-j]) / j
                    dp[i][k] = max(dp[i][k], dp[i-j][k-1] + tmp)
        return dp[n][K]