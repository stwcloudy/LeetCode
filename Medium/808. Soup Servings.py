'''
提供2种汤供应,有等概率提供4种供应方式:
1. 100ml A, 0ml B
2. 75ml A, 25ml B
3. 50ml A, 50ml B
4. 25ml A, 75ml B
初始一共Nml A和B 求A先供应完的概率加上两者同时供应完的概率的一半。

解法:
记忆化dp
dp[a,b]表示当前(a,b)时所求结果的概率,最后返回的是dp(N,N)
dp对于小的N来说没问题,对于大的N 由于不存在直接供应100mlB的情况，所以N越大 所求结果越接近于1 在误差允许范围内 指定当N大于某个值时都返回1即可.
'''
class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N > 4800:
            return 1.
        dp = collections.defaultdict(float)
        def dfs(a,b):
            if (a,b) in dp:
                return dp[(a,b)]
            if a == 0 and b == 0:
                return 0.5
            elif a == 0:
                return 1
            elif b == 0:
                return 0
            tmp = 0
            tmp += 0.25*dfs(max(a-100,0),b)
            tmp += 0.25*dfs(max(a-75,0),max(b-25,0))
            tmp += 0.25*dfs(max(a-50,0),max(b-50,0))
            tmp += 0.25*dfs(max(a-25,0),max(b-75,0))
            #print (tmp)
            dp[(a,b)] = tmp
            return tmp
        return dfs(N,N)