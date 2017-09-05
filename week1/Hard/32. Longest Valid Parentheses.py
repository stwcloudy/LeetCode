"""
思路:
似乎括号匹配的题都离不开栈的使用,我在这里用了一个栈
栈里存储的是上一个不合法的位置(初始化为-1),这样的话
每当我匹配一个合法的括号之后,都用当前位置减去栈顶处的位置,即得到目前匹配到的合法括号的长度
最后遍历完整个字符串之后得到可以得到最终的最长合法字符串的长度

法二:
在discuss中看到的一个用dp来做的
https://leetcode.com/problems/longest-valid-parentheses/discuss/
思路是用dp[i]表示以s[i]结尾的最大合法匹配括号
1.当s[i] == '(',此时dp[i] = 0,因为没有以'('结尾的合法匹配
2.当s[i] == ')':
    2.1 如果s[i-1] =='(',则dp[i] = dp[i-2] + 2(所加的2是s[i-1],s[i]构成的合法匹配)
    2.2 如果s[i-1] == ')',找到i-1-dp[i-1]的位置(该位置是以s[i-1]结尾的合法匹配的上一个字符),如果
        s[i-1-dp[i-1]] =='(',则其与s[i]匹配:dp[i] = dp[i-1]+2+dp[i-2-dp[i-1]]
        这三部分分别是以s[i-1]结尾的长度+(s[i-1-dp[i-1]],s[i]) + s[i-1-dp[i-1]]之前字符结尾的长度
最后,一个小优化是上述2中的两种情况可以合并,因为最开始初始化dp的值都为0,s[i-1] =='('时,dp[i-1] = 0

注意要判断i-1-dp[i-1],i-2-dp[i-1]等位置的合法性
"""
##Solution 1
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        st = [-1]
        for i in range(len(s)):
            if st[-1] != -1 and s[st[-1]] == '(' and s[i] == ')':
                st.pop()
                res = max(res,i-st[-1])
            else:
                st.append(i)
        return res

##Solution 2

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        dp = [0]*len(s)
        res = 0
        for i in range(1,len(s)):
            if s[i] == ')' and i - 1 - dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                dp[i] = dp[i-1] + 2 + (dp[i-2-dp[i-1]] if i-2-dp[i-1]>=0 else 0)
                res = max(res,dp[i])
        return res