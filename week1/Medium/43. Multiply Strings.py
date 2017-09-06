"""
高精度乘法,模拟就行,题目限制不需要考虑正负数和前导0的情况

"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        n,m = len(num1),len(num2)
        tot = n + m
        res = [0]*tot
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(n):
            for j in range(m):
                res[i+j] += int(num1[i])*int(num2[j])
        for i in range(tot - 1):
            res[i+1] += res[i]/10
            res[i] = str(res[i]%10)
        if res[-1] == 0:
            res.pop()
        else:
            res[-1] = str(res[-1])
        return ''.join(res[::-1])