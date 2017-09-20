"""
思路:
动态规划 dp[i]表示前i个字符有多少种解码方式:
1.s[i-1] != '0': dp[i]至少有dp[i-1]种方式
2.int(s[i-2:i]) <= 26 则dp[i] += dp[i-2]
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        pre,cur,post = 0,1,0
        for i in range(1,len(s)+1):
            post = 0
            if s[i-1] != '0':
                post = cur
            if i >= 2 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                post += pre
            pre,cur = cur,post
        return post