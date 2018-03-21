"""
找出一个只有'A','C','G','T'组合成的字符串中的出现超过一次的长度为10的子串
法1:
用python解答的话，只需要用两个set集合，其中一个set，seen存已有子串，当前子串若在seen中已有，说明其存在，将其添加到repeated集合中，
repeated使用集合的好处是当一个子串重复出现大于2次 则不会重复添加。时间为O(N),空间为O(N)

法2：
法1一个字符是一个字节，存一个子串需要10个字节，可根据本题字符的特殊性（只包含四种）来使用位操作：
'A' -- >>00
'C' -- >>01
'G' -- >>10
'T' -- >>11
这样一个字符用2bit 一个串只需要2*10=20bit存储
代码如下：

"""
法1:
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        res = []
        if len(s) <= 10:
            return res
        
        for i in range(len(s) - 10 + 1):
            tmp = s[i:i+10]
            if tmp in seen:
                repeated.add(tmp)
            else:
                seen.add(tmp)
                
        return list(repeated)

 法2:
 class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        res = []
        if len(s) <= 10:
            return res
        bits = {'A':0,'C':1,'G':2,'T':3}
        val = 0
        for i in range(len(s)):
            val = ( (val << 2) | bits[s[i]]) & 0xfffff
            if i < 9:
                continue
            if val in seen:
                repeated.add(s[i-9:i+1])
            else:
                seen.add(val)
        return list(repeated)
        