"""
先处理特殊情况:
1.如果a%mod == 0 : 不管多少次方 最后的结果一定是0
2.如果a>mod:则可将a替换为a%mod (a = x*mod + a%mod,乘b个a之后结果是b个(a%mod)相乘再%mod)
思路一:
这题的幂很大用数组表示,但是基于10进制的格式还是可以用快速幂来解决
这里有一个引理:
(a*b)%c = ((a%c)*(b%c))%c
本题中a^b = a^(sigma(bi*10^i))(其中i取0-len(b)-1,sigma表示求和)
          = prod((a^10^i)^bi)(prod表示连乘)
所以思路是先将a^(10^i)先保存在一个数组中,最后再求新数组的bi次幂
而每一次求幂 都调用快速幂的函数 且中间值和结果要取模
由于计算a^(10^i) 都是使用a^(10^(i-1))作为基数,循环最多4次,求该新数组一共4*|b|次
求结果时,b[i] < 10 所以也是调用4*|b|,一共8|b|次的时间复杂度
思路二:
a^b%c 有循环出现,假设循环节是m,则我们只需要将b%m,就可以知道余数为多少
先用一个数组保存循环中的每一个位置上的余数(从1次幂开始找余数直至重复)
再将b%m(过程中每一步都要%m,以免溢出)求得a^b%c的位置,返回该位置上的相应余数即可
时间复杂度为O(|b|+m)
思路三:
利用欧拉函数降幂公式(没找到证明过程,自己没实现代码)
"""

###Solution1
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        mod = 1337
        b = b[::-1]
        if a%mod == 0:
            return 0
        if a > mod:
            a = a%mod    
        def Pow(a,n):
            tmp = 1
            while n:
                if n&1:
                    tmp = (tmp*a)%mod
                n >>= 1
                a = (a*a)%mod
            return tmp%mod
        bpow10 = [0]*len(b)
        bpow10[0] = a%mod
        for i in range(1,len(b)):
            bpow10[i] = Pow(bpow10[i-1],10)
        for i in range(len(b)):
            res = (res%mod * Pow(bpow10[i],b[i])%mod)%mod
        return res

###Solution2
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        mod = 1337
        if a%mod == 0:
            return 0
        if a > mod:
            a = a%mod    
        def work(b,rlen):
            pos = 0
            for i in range(len(b)):
                pos = (pos*10 + b[i])%rlen
            return pos
        def getRemainder(a,mod):
            showup = [False]*mod
            rem = a % mod
            r = []
            while not showup[rem]:
                showup[rem] = True
                r.append(rem)
                rem = (rem*a)%mod
            return r
        r = getRemainder(a,mod)
        rem = work(b,len(r))
        rem = len(r) - 1 if rem == 0 else rem
        return r[rem-1]