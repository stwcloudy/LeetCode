"""
本题是求[m,n]区间中所有数的与的结果
通过几组数据的分析，本题是求m,n二进制形式的最左部分的公共部分

法1:
要求相同的左半部分，则m!=n时 每次将这两个数都右移一位，记录下移动的次数，
最后移动到结果相同时(此时只剩下公共部分) 所求结果即为此时的值左移所记录的次数
因为当m!=n时，最右一位(最低位)的与一定为0,所以循环中两个数先移动

法2：
相邻两个数的最低位与一定为0,所以可以循环(m<n)时，每次n&(n-1)消掉最低位的1
"""
法1：
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return (m <<i)

法2：
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m <n:
            n = n & (n - 1)
        return n