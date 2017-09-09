"""
简单题,注意先处理负号和越界情况就行
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        flag = 1
        if x < 0:
            flag = -1
        n = abs(x)
        rev = 0
        while n:
            rev = rev*10 + n%10
            n /= 10
            if rev > 2147483647:
                return 0  
        return flag*rev