"""
法一:
该题字符串匹配问题时,可以用递归来做：
首先判断递归的基础返回条件,如果p为空,则返回s是否为空
1.若匹配的下一个字符p[j+1] != '.',则判断当前s[i] == p[j] or p[j] == '.',
若满足则递归判断下一个isMatch(s+1,j+1),否则 返回False
2.若p[j+1] == '*',则返回isMatch(s,p+2)[*匹配0个前面字符],或isMatch(s+i,p+2)[i= 1,2,3,...匹配多个字符]
法二:
动态规划解
dp[i][j] 表示s[0-i-1],p[0-j-1]的匹配情况,同样分两种情况:
1. p[j-1] != '*':s[i-1] == p[j-1] or p[j-1]=='.',则 dp[i][j] = dp[i-1][j-1];
2. p[j-1] == '*':
    2.1 若'*'匹配0个前字符,则p[i][j] = p[i][j-2]
    2.2 '*'匹配一个以上的前字符,则p[i][j] = p[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')
"""

### recursive solution
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        if len(p) == 1 or p[1] != '*':
            if s and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:],p[1:])
            else:
                return False
        else:
            i = -1
            while i < len(s) and (i < 0 or s[i]==p[0] or p[0] == '.'):
                if self.isMatch(s[i+1:],p[2:]):
                    return True
                i += 1
            return False

###dp solution
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False]*(len(p)+1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1,len(p) + 1):
            if i >= 2 and p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1,len(s) + 1):
            for j in range(1,len(p) + 1):
                if p[j-1] != '*':
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return dp[len(s)][len(p)]