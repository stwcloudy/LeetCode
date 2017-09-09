"""
思路:
一开始想用一个新的字典记录s当前窗口中的t中的字符出现的个数
但是不知道怎么判断right指针的停止位置
所以转换了一下思路,还是有一个字典记录t中的字符与其个数,维护窗口的左右边界
用一个remain变量表示t中字符不在窗口中的个数,当remain=0时,表示该窗口中已经包含所有t中字符
再收缩left边界,维护最小窗口的起始点和最小长度
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''
        m,n = len(s),len(t)
        if m < n :
            return ''
        d = {}
        for ch in t:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        pos,minlen = -1,m+1
        left,right,remain = 0,0,n
        while right < m:
            if s[right] in d:
                if d[s[right]] > 0:
                    remain -= 1
                d[s[right]] -= 1
                while remain == 0:
                    if minlen > right - left + 1:
                        pos = left
                        minlen = right - left + 1
                    if s[left] in d:
                        if d[s[left]] == 0:
                            remain += 1
                        d[s[left]] += 1
                    left += 1
            right += 1
        return s[pos:pos+minlen] if pos != -1 else ""