"""
康托展开
按字典序的全排列的序号=a[n-1]*(n-1)!+a[n-2]*(n-2)!+...+a[0]*0!
其中a[i]表示第i位之后比num[i]小的数字的个数
该序号是从0开始的,所以第k个全排列其序号表示为k-1
再根据逆康托展开求全排列即可
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
        vis = [False]*(n+1)
        k -= 1 #序号从0开始
        for i in range(n-1,-1,-1):
            xishu = k / fac[i]
            k %= fac[i]
            target,num = 1,0
            while num <= xishu:
                if not vis[target]:
                    num += 1
                target += 1
            target -= 1
            vis[target] = True
            res += str(target)
        return res