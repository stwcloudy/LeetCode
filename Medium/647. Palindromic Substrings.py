'''
找出字符串中回文子串的个数
3种方法 按照runtime由高到低:
1. 动态规划,dp[i][j] = True 表示子串s[i:j+1]是回文串,按照子串长度从1开始更新没找到一个true 结果加1
2. 围绕中心点，向两边拓展，一共有2*n-1个中心点(包括字符位置和字符字符间的空隙) 也是每找到一个就加1
3. manacher算法，该算法原本是寻找最长回文串长度的，但是由于记录了每个位置往外拓展的回文半径，所以可以借此来求出所有的回文子串的个数
由于回文串abccba cc,bccb abccba都是回文串，所以找到回文半径之后P[i]／2 即为以当前i为中心点到回文串数目.
'''
法1:（387ms）
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = n
        for i in range(n):
            dp[i][i] = True
            if i != n-1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        for l in range(3,n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res += 1
        return res

法2:(112ms)
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for center in range(2*n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
法3:(48ms)
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        pos,maxright = 0,0
        P = [0]*n
        for i in range(n):
            #print(i)
            if i < maxright:
                P[i] = min(maxright - i, P[2*pos-i])
            else:
                P[i] = 1
            while i-P[i] >= 0 and i + P[i] < n and s[i-P[i]] == s[i+P[i]]:
                P[i] += 1
            if i + P[i] - 1 > maxright:
                maxright = i + P[i] - 1
                pos = i
        #print (P)
        return sum(length//2 for length in P)
                
        