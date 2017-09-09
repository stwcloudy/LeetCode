"""
该题关键在于两点:
1.判断何种情况下会溢出,以及结果的正负性
2.题目要求不能采用乘,除,模的操作
比较容易想到的是每次减一个除数就加1,但是这种方法在极端情况下会TLE(999999999,1)
所以只能借助于位操作
方法:
每次将除数尽可能的左移接近被除数,左移一位,本次结果要也要左移1位,当除数最大且小于被除数了
被除数-移位之后的除数,再进行重复操作，直到被除数小于除数
由于移位运算增长得很快,所以被除数也是以指数级减少
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        if divisor == 0 or (dividend == INT_MIN and divisor == -1):
            return INT_MAX
        if abs(dividend) < abs(divisor):
            return 0
        flag = 1
        if dividend < 0:
            flag *= -1
        if divisor < 0:
            flag *= -1
        x,y = abs(dividend),abs(divisor)
        res = 0
        while x >= y:
            tmp,lm = y,1
            while x > (tmp << 1):
                tmp <<= 1
                lm <<= 1
            res += lm
            x -= tmp
        return res*flag