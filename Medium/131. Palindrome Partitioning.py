"""
解法一:
枚举每一个可能的分割点
若当前分割点前的子串为回文串,则将其加入到可能的结果当中,递归求解剩余串的回文子串
解法二:
利用动态规划来解
1.受求最长回文子串的启发,在本题中定义dp[i][j]表示子串s[i-j]是否是回文串
2.用res[i]表示到s[i](不包括s[i])的前部分字符串的合法划分,已知res[0] = [[]]
3.枚举i从1-n的所有值,并寻找合法的left,每次找到left(s[left:i]回文,则将s[left:i]添加至res[left]的
每一个划分中,将更新后的划分赋给res[i]
最后结果为res[n]
"""
###Solution1
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def isPalindrome(tmps):
            i,j = 0,len(tmps)-1
            while i < j:
                if tmps[i] == tmps[j]:
                    i += 1
                    j -= 1
                else:
                    break
            if i >= j:
                return True
            return False
        def dfs(s,pal,res):
            if len(s) == 0:
                res.append(pal)
                return
            for i in range(len(s)):
                if isPalindrome(s[:i+1]):
                    dfs(s[i+1:],pal+[s[:i+1]],res)
        
        dfs(s,[],res)
        return res

###Solutin2
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        res = [[] for _ in range(n+1)]
        res[0].append([])
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i < n-1 and s[i] == s[i+1]:
                dp[i][i+1] = True
        for l in range(3,n+1):
            for i in range(0,n-l+1):
                j = i + l - 1
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        for i in range(1,n+1):
            for left in range(0,i):
                if dp[left][i-1]:
                    for pal in res[left]:
                        res[i].append(pal+[s[left:i]])
        return res[n]