"""
注意判断负数情况直接返回false
其余和数字反转一样,求出反转数字之后判断两者是否相等即可
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        tmp = x
        while tmp:
            rev = rev*10 + tmp%10
            tmp /= 10
        print rev
        if rev == x:
            return True
        return False