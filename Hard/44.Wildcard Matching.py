"""
这题和之前那道'*'匹配前个字符多次的有点类似
解法一:
还是可以采用动态规划来做
dp[i][j]表示的是s[0-i-1],p[0-j-1]是否匹配
分两种情况
1.p[j-1] != '*':dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
2.p[j-1] == '*':
    2.1 '*'匹配0个字符,dp[i][j] = dp[i][j-1]
    2.2 '*'匹配多个字符,dp[i][j] = dp[i-1][j] 表示之前匹配了字符
dp的时间复杂度是O(nm) 空间复杂度也是O(nm),但是可以降低空间复杂度
解法二:
http://shmilyaw-hotmail-com.iteye.com/blog/2154716
这个地方有详细的介绍
大意是记录下'*'出现时，两个串中的位置.i_star,j_star由于'*'能匹配0-多个字符
所以从i_star和j_star的下个位置开始正常匹配,遇到不能匹配的,i_star+1,j串的指针
再回溯到j_star的下个位置继续匹配
要注意的就是s匹配完之后p串之后可能还有字符,若都为'*'则表示能匹配 否则不能
"""



###Solution 1
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        j_star = -1
        i_start = -1
        i,j = 0,0
        while i < len(s):
            if j < len(p) and p[j] == '*':
                i_star = i        #记录*出现时s,p字符串的位置
                j_star = j
                j = j_star + 1
            elif j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            else:
                if j_star == -1: #当前位置不匹配且之前没有出现过* 表明字符串不匹配
                    return False
                i_star += 1  #j回溯到*所在位置,i回溯到上一次匹配的起点的下一个位置
                i = i_star
                j = j_star + 1
        while j < len(p):
            if p[j] == '*':
                j += 1
            else:
                break
        return j == len(p)

###Solution2
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1,len(p)+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[len(s)][len(p)]