'''
题意: 在一个数组中找出子数组中最大值在边界[L,R]之间的个数
子数组是连续的，由于最大值不能超过R 所以原数组中大于R的值就把数组分割成多个子数组，分别在分割出来的子数组中求 不影响结果.
所以可以用一个start标记上一个不合法的位置，每遇到一个>=L的数 从start之后包含该数的子数组都合法，都要加1，所以用end标记当前遇到的>=L的数的位置

也可以用动态规划来解:
dp[i]表示以i结尾的子数组中满足条件的个数
1.A[i] < L: 以A[i]结尾的满足条件的个数即是把以A[i-1]结尾的子数组添加上A[i]所至,所以dp[i] = dp[i-1]
2.A[i] > R: dp[i] = 0
3.L <= A[i] <= R: 上一次不合法位置为start 则他之后的所有位置A[start+1->i], A[start+2->i],...都为新的合法的子数组，个数为i- start, dp[i] += i - start

两方法基本意思相同

'''
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        start, end, res = -1, -1, 0 
        n = len(A)
        for i,num in enumerate(A):
            if A[i] > R:
                start = i
                end = i
                continue
            if A[i] >= L:
                end = i
            res += end - start
        return res

dp solution:
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res, dp = 0, 0
        prev = -1
        for i in range(len(A)):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R:
                dp = 0
                prev = i
            if L <= A[i] <= R:
                dp = i - prev
                res += dp
        return res