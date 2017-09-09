"""
构造对应转换的字典,在按照所给罗马字符串相加即可
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtoi = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        res = 0
        for i in range(0,len(s)):
            if i > 0 and rtoi[s[i-1]] < rtoi[s[i]]:
                res += rtoi[s[i]] - 2*rtoi[s[i-1]] ##-2倍是因为前面已经加过一次了
            else:
                res += rtoi[s[i]]
        return res