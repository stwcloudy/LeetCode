'''
给定两种类型的瓷砖,给长度N求出铺满2*N的一共有多少种铺法
x xx  xx   x
x 	  x	  xx
f(N)表示N时候的铺法种类，则有如下规律
1. 最后一块竖着铺 一共有f(N-1)种
2. 最后两列是被横着铺盘, 一共有f(N-2)种
3. 最后状态为
xyy	  xxy    xyyz. xxyy
xxy   xyy 或者xxzz  xzzy ,..., 一共有2*(f(N-3) + f(N-4) + ... + f(0))
所以f(N) = f(N-1) + f(N-2) + 2*(f(N-3) + f(N-4) + ... + f(0))
		= f(N-1) + (f(N-2) + f(N-3) + 2*(f(N-4) + ... + f(0))) + f(N-3) 
		= f(N-1) + f(N-1) + f(N-3)
		= 2*f(N-1) + f(N-3)
'''
class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 2:
            return N
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,N+1):
            dp[i] = dp[i-3] + 2*dp[i-1]
        return dp[N]%(10**9+7)