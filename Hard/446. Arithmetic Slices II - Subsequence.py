"""
思路:
这题自己一开始也是往<差值,个数>这个思路去想的,但是错误的理解成了,下标的差值,后来看了别人的思路之后才
理解过来。
dp[i],是一个字典,字典的key是等差数列的公差diff,value是以a[i]结尾的差值为diff的等差数列切片的个数
用dp[i][diff]表示
(字典默认值设为0 所以调用python库中的defaultdict来生成一个类似字典的对象)
怎么更新dp[i]的值呢,对于a[i]之前的数字a[j](0<=j<i) 两者之间差值为diff=a[i]-a[j]
则a[j],a[i]构成了差值为diff的两个数切片,之前的413题中,dp中所存的值必须是个数大于等于3才加1
但是此处必须先+1(即便不是完整的三个数构成等差),假设后面有个数a[k]也和a[i]构成diff的两个数,在更新dp[k]
时,如果按照常规的情况两个数的设为1则dp[k]中将不会包含a[j],a[i],a[k]这种合法情况
所以为了后面的计算,有两个数时就应加1,而如果dp[j]中有差值diff,dp[i][diff] += dp[j][diff]
注意在计算总的个数的时候,更新的是dp[i][diff],但是加的却是dp[j][diff],因为dp此时dp[j][diff]中的个数才是完整的等差数列的个数
而dp[i]中还包含了2个数的情况
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        tot = 0
        from collections import defaultdict
        dp = [defaultdict(int) for _ in A]
        for i in range(n):
            for j in range(i):
                dp[i][A[i]-A[j]] += 1
                if A[i]-A[j] in dp[j]:
                    dp[i][A[i]-A[j]] += dp[j][A[i]-A[j]]
                    tot += dp[j][A[i]-A[j]]
        return tot