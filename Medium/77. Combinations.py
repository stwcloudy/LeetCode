"""
解法一:利用公式C(n,k) = C(n-1,k) + C(n-1,k-1)递归求解
解法二:直接回溯递归(但是在python下(20,16)时会超时)
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if k == 0:
            return [[]]
        def helper(n,k,comb):
            if n == k:
                return [comb+[i for i in range(1,n+1)]]
            if k == 1:
                tmp = []
                for i in range(1,n+1):
                    tmp.append(comb+[i])
                return tmp
            return helper(n-1,k-1,comb+[n]) + helper(n-1,k,comb)
        res = helper(n,k,[])
        return res