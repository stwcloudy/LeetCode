"""
思路1:
可以通过计算得知长度为n(n>=3)的等差数列的切片一共有n*(n-3)/2+1种,所以我的想法是
在整个数列中求出有多少种不同的等差数列(每个单独的等差数列的长度最大),记录下每个数列的长度,最后按照公式累加起来即可
比如:
1 2 3 4 4 4 5 6 6 6 
一共4个不同的等差数列,[1,2,3,4],[4,4,4],[4,5,6],[6,6,6]
所以最后结果是3+1+1+1 = 6
思路2::
动态规划:
dp[i]表示以a[i]结尾的数列的不同的等差数列切片有多少,转移方程为:dp[i] = dp[i-1] + 1 if a[i-1] - a[i-2] == a[i] - a[i-1]
如果条件成立(a[i-1] - a[i-2] == a[i] - a[i-1]) 那所有以a[i-1]结尾的等差数列再加一个a[i]也是等差数列,一共dp[i-1]个,而
a[i-2],a[i-1],a[i]是一个新的+1
所以dp[i] = dp[i-1] + 1
最后结果res = sigma(dp[i])
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A) 
        diff = [-1]*n
        for i in range(1,n):
            diff[i] = A[i] - A[i-1]
        arithmetic = []
        s,l = 0,1
        for i in range(1,n-1):
            if diff[i] == diff[i+1]:
                l += 1
            else:
                if l >= 2:
                    arithmetic.append((s,l+1))
                    s = i
                    l = 1
        if l >= 2:
            arithmetic.append((s,l+1))
        res = 0
        for _,l in arithmetic:
            res += l*(l-3)/2 + 1
        return res
                    