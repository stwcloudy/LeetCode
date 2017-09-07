"""
快速幂的模板题,根据幂的二进制位决定是否乘
注意判断幂的正负即可
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        absn = abs(n)
        res = 1
        while absn:
            if absn & 1:
                res = res*x
            absn >>= 1
            x = x*x
        if n < 0:
            return 1.0/res
        return res