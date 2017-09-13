"""
法一：
这种方法是比较容易想到的，动态规划解,
dp[i][j]=True 表示s[i-j]是回文子串,该dp的动态转移方程为dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
先初始化好长度为1和2时的dp的值，再从长度为3开始枚举每一个起始点i,每次更新时都记录当前的pos和最大长度
最后结果为s[pos:pos+maxLen]
动态规划的解法时间复杂度为O(n^2)
法二:
Manacher法,它是利用了回文穿本身的一些特性减少时间复杂度,
没图片讲起来比较抽象,这贴一个我自己看的关于此算法的讲解http://www.cnblogs.com/biyeymyhjob/archive/2012/10/04/2711527.html
大概讲述起来该算法在于先将所有可能的字符串长度都转换为2*n+1的字符串(在每个字符的两边插入一个特殊字符如'#')
然后用一个P[i]数组表示以是s[i]为中心的回文串的半径(比如#a#b#a#,P[3] = 4)举个例子
S     #  a  #  b  #  b  #  a  #  b  #  c  #  b  #  a  #
P     1  2  1  2  5  2  1  4  1  2  1  6  1  2  1  2  1
而原始串中的最长回文串长度刚好是最大P[i]-1
该算法巧妙的地方在于计算P[i],设置两个辅助变量mx,id
id:记录当前最右边界的回文串的中心位置
mx:mx = id + P[id],即最大回文串的右边界位置处
在计算某个P[i]时,若i > mx,则只能从当前开始往两边拓展做,而i<mx时,由于回文串的对称性质可以得到：
P[i] = min(mx-i,P[j]),其中j = 2* id - i 是i关于id的对称点,若P[j] < mx - i 表示P[i]的回文长度被
包含在mx之内,否则则至少为mx-i,剩下的继续根据两边字符相等情况拓展
每次更新后 若i + P[i] > mx,则要更新id和mx，同时记录最大回文串的pos
由于mx的位置每次都是向前更新,而只有在mx这一位开始才比较,所以时间复杂度为O(n)
"""

###Solution1
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False]*(len(s)) for _ in range(len(s))]
        pos,maxLen = 0,1
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) - 1 and s[i] == s[i+1]:
                pos = i
                maxLen = 2
                dp[i][i+1] = True
        for l in range(3,len(s)+1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    pos = i
                    maxLen = l
        return s[pos:pos+maxLen]


###Solution2
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#'+'#'.join(s)+'#'
        p = [0]*len(s)
        mx,idx,pos,maxLen = 0,0,0,0
        for i in range(1,len(s)):
            if i < mx:
                p[i] = min(p[2*idx-i],mx-i)
            else:
                p[i] = 1
            while i - p[i] >= 0 and i + p[i] < len(s) and s[i-p[i]] == s[i+p[i]]:
                p[i] += 1
            if p[i] > maxLen:
                pos = i
                maxLen = p[i] ##扩展后的回文半径-1刚好是该回文串的长度
            if i + p[i] - 1 > mx:
                idx = i
                mx = i + p[i] - 1
        return s[pos-maxLen+1:pos+maxLen].replace('#','')
        