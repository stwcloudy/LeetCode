'''
朴素解法O(N*M)
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_len = len(strs[0])
        for i in range(1,len(strs)):
            min_len = min(min_len,len(strs[i]))
        print min_len
        res = ''
        for i in range(min_len):
            ch = strs[0][i]
            for j in range(1,len(strs)):
                if ch != strs[j][i]:
                    return res
            res += ch
        return res