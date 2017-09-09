"""
一开始看这题,觉得只要拿上一题得到的结果中最少的元素的分解-1就是答案,结果超时了
后来先预处理了dp[i][j] 表示s[i-j]是否是回文串,再用res[i][j]表示s[i-j]最少需要多少次
枚举长度,起点和切割点,复杂度为O(n^3) 又超时了
最后有人提醒之后,将res[i][j]改为cut[i]表示s[0-i]的切割次数
最开始初始化cut[i] = i(因为s[0-i]最多切割i次表示无回文子串)
然后遍历i的位置 如果dp[0][i]是回文串 则直接赋0 处理下一个
否则,遍历(0-i)的切割点,找最小值 时间复杂度为O(N^2) python代码提交688ms
解法2：
预处理子串s[i-j]是否回文,遍历了两遍O(n^2)所以采用中心枚举法;
依旧维护数组cut,分奇数,偶数的情况向两边扩展 每当扩展出一个回文串之后 cut[i+r+1] = min(cut[i+r+1],cut[i-r]+1)
这里cut与法一种略有不同的是,cut[i]表示的是s[0-i-1]的切割次数
只需一遍O(N^2) 比法一快了200ms左右
(有一点要提的是如果加上先处理最小切割为0,1的情况 时间一下就到30多ms了)
"""
###Solution1
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut = [0]*n
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i < n-1 and s[i] == s[i+1]:
                dp[i][i+1] = True
        for l in range(3,n+1):
            for i in range(0,n-l+1):
                j = i + l - 1
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        if dp[0][n-1]:
            return 0
        for i in range(n):
            cut[i] = i
            if dp[0][i]:
                cut[i] = 0
                continue
            for j in range(0,i):
                if dp[j+1][i]:
                    cut[i] = min(cut[i],cut[j]+1)
        return cut[n-1]

###Solution2
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        ###先处理0,1的情况 可加速程序
        # if s[:] == s[::-1]:
        #     return 0
        # for i in range(n):
        #     if s[:i+1] == s[:i+1][::-1] and s[i+1:] == s[i+1:][::-1]:
        #         return 1
        cut = [i for i in range(-1,n)]
        for i in range(0,n):
            oddr,evenr = 0,0
            while i-oddr >= 0 and i+oddr < n and s[i-oddr] == s[i+oddr]:
                cut[i+oddr+1] = min(cut[i+oddr+1],cut[i-oddr]+1)
                oddr += 1
            while i - evenr >= 0 and i+1+evenr < n and s[i-evenr] == s[i+1+evenr]:
                cut[i+2+evenr] = min(cut[i+evenr+2],cut[i-evenr]+1)
                evenr += 1
        return cut[-1]