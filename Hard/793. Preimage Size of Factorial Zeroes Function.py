'''
题意：求出阶乘末尾0的个数为k的数字的个数
对于n!来说，末尾出现的0的个数只与(2,5)的因子数有关，而2出现的次数远远大于5 所以只与5有关。如何计算因子5的个数？
f[n] = [n/5] + [n/25] + [n/(5^3)] + ...
解法1:
对于n!的末尾0的个数f[n],有性质 f[i] >= f[j] if i >= j
所以可用二分的思想来做， 取上界和下界 分别求出 <=k 的个数和<=(k-1)的个数 则最后等于k的结果就等于两者的差
在上界的初始化时，我们知道[n/5]贡献了最多的5, 所以如果x是有k个0的最大的数 那么有x <= 5*(k+1)

解法2:
如果将阶乘末尾0的个数与n画在坐标系中，可以知道每当遇到5的倍数时k值都会越阶，n = 0-4 -> k = 0, n = 5 -> k = 1;
n = 6-9 -> k = 1, n = 10 -> k = 2 ,..., n = 21-24 -> k = 4, n = 25 -> k = 6; 此处遇到25，5的因子为2 所以直接跳过k=5 k变为6
所以其图像是一个阶梯式上升的图像,并且每遇到25的倍数 就会多越一级，于是在k中只有部分合法， 且合法的k值 得到的结果都是5个。
所以还是用2分查找k，如果存在这样的值等于所要求的K 则说明合法，返回5 否则 不合法， 返回0

'''
解法1:
class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        
        def count(k):
            l, r = 0, 5*(k+1)
            while l <= r:
                mid = (l + r) >> 1
                count, num = 0, mid
                while num:
                    count += num // 5
                    num //= 5
                #print (count)
                if count <= k:
                    l = mid + 1
                else:
                    r = mid - 1
            #print (r)
            return r
        return count(K) - count(K-1)

 解法2:
 class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        
        def count(k):
            l, r = 0, 5*(k+1)
            while l <= r:
                mid = (l + r) >> 1
                count, num = 0, mid
                while num:
                    count += num // 5
                    num //= 5
                #print (count)
                if count < k:
                    l = mid + 1
                elif count > k:
                    r = mid - 1
                else:
                    return 5
            return 0
        return count(K)