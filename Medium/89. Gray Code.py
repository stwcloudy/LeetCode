"""
法一:
可以发现,n位gray code对应的二进制分别是0+(n-1)位本身和1+(n-1)位逆序构成
n = 3 [00,01,11,10]
000 001 011 010, 100 101 111 110
法二:
按照公式 : gray code = binary code ^ (binary code >>1)
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        res = [0,1]
        for i in range(1,n):
            tmp = res
            for num in tmp[::-1]:
                tmp.append((1<<i)+num)
            res = tmp
        return res

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1<<n):
            res.append((i>>1)^i)
        return res
        