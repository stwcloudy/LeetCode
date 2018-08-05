"""
思路:
最多只允许两次交易,可转化为最多允许k次交易的求解问题
假设dp[k][i]表示截止到第i天,k次交易的收益(最后一次交易不一定是以第i天结束),则转移方程表示为:
dp[k][i] = max(dp[k][i-1],max(dp[k-1][j]-prices[j])+prices[i]) 其中 0<=j<i,
则最后的答案为dp[K][n-1]，n为天数
可以优化为O(n)的空间复杂度,时间复杂度为O(Kn)
dp = [0]*n
for k in range(1,K+1):
    tmp = dp[0] - prices[0]
    for j in range(1,n):
        pre = dp[j]   ##表示dp[k-1][j]
        dp[j] = max(dp[j-1],tmp + prices[j])
        tmp = max(tmp,pre-prices[j])
return dp[n-1]
解法2:
比较巧妙的解法,最多两次交易,对应4个状态,第一次持有,第一次抛出,第二次持有,第二次抛出
假设初始时没有钱,第一次买入时需要最小化所借的钱以使得profit最大,即最大化hold1,买入之后
release1表示第一次卖出,此时需要最大化剩余的钱即prices[i]-hold1
同样hold2表示第一次卖出之后再买第二支股票,还剩的钱最大化release1-prices[i]
最后最大的profit就表示为release2,prices[i]+hold2
循环中这四个变量不需要表示为上一次和本次的区分,因为如果当天的prices[i]高于之前的hold1,则
hold1不变依旧表示为上一次的结果,所以用它去更新其他值不会有问题
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        K = 2
        n = len(prices)
        dp = [[0]*n for _ in range(K+1)]
        for k in range(1,K+1):
            tmp = dp[k-1][0] - prices[0]
            for j in range(1,n):
                dp[k][j] = max(dp[k][j-1],tmp + prices[j])
                tmp = max(tmp,dp[k-1][j]-prices[j])
        return dp[K][n-1]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        inf = 0x7fffffff
        buy1,sell1,buy2,sell2=-inf,0,-inf,0
        for i in range(len(prices)):
            buy1 = max(buy1,-prices[i])
            sell1 = max(sell1,buy1+prices[i])
            buy2 = max(buy2,sell1-prices[i])
            sell2 = max(sell2,buy2+prices[i])
        return sell2
