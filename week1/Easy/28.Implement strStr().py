"""
这题的测试样例应该很简单,朴素的算法就能过.
但是借此复习一下KMP算法
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def getNext():
            Next = [-1]*len(needle)
            k,j = -1,0
            while j < len(needle) - 1:
                if k == -1 or needle[k] == needle[j]:
                    k += 1
                    j += 1
                    if needle[j] == needle[k]:  ##优化
                        Next[j] = Next[k]
                    else:
                        Next[j] = k
                else:
                    k = Next[k]
            return Next
        i,j = 0,0
        Next = getNext()
        print Next
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = Next[j]
        print j
        if j == len(needle):
            return i - j
        return -1
        