"""
了解罗马数字和阿拉伯数字的转化规则不难
与其对应的是将相应的罗马数字转化为阿拉伯数字
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i = 0
        while num and i < len(val):
            count = num / val[i]
            res += roman[i]*count
            num %= val[i]
            i += 1
        return res