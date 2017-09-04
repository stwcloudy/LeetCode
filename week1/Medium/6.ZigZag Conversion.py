"""
法一:
寻找规律之后发现每一行有个基础间隔为2*nomRows-2,而非0行和最后一行时,还会多加上一个j+basediff-2*i的字符
按照此模拟即可

法二:
按照描述的规律直接模拟即可,用一个list存储结果,每行的元素存储在一个list元素中，
用一个step标记为1或-1,1的时候向下增加网list中添加,为-1则表示向上走的路径,模拟
完成之后即得到结果

"""

###Solution1
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ''
        basediff = 2*numRows - 2
        for i in range(numRows):
            for j in range(i,len(s),basediff):
                res += s[j]
                if  i != 0 and i != numRows - 1:
                    if j + basediff - 2*i < len(s):
                        res += s[j + basediff - 2*i]
        return res

###Solution2
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        res = ['']*numRows
        idx,step = 0,0
        for i in range(len(s)):
            res[idx] += s[i]
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(res)