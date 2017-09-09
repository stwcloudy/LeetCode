"""
思路：
用一个list维护当前不重复子串，从第二个元素遍历到串尾，其中list长度最大时即为所求结果，
如果当前判断字符没有出现在list中，则直接添加进list，否则遍历list直到找到与当前字符相
同的位置，将这个位置及其以前的字符全部删除，添加进当前字符，形成新的list
每一个位置的字符操作之后与当前结果比较，取两者较大者

法二（借鉴）：
也是维护窗口，但是用left表示窗口左边界(窗口不包括left所在位置),用一个字典存储窗口中元素位置，
若当前字符出现，则left直接更新为该字符在字典中存储的位置
def lengthOfLongestSubstring(self, s):
    charAt = {}
    start = -1 
    ans = 0
    for i in range(len(s)):
        if s[i] in charAt and start < charAt[s[i]]:
            start = charAt[s[i]]
        else:
            ans = max(ans,i - start)
        charAt[s[i]] = i
    return ans
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 1
        d = [s[0]]
        for i in range(1,len(s)):
            if s[i] not in d:
                d.append(s[i])
            else:
                while d[0] != s[i]:
                    d.remove(d[0])
                d.remove(d[0])
                d.append(s[i])
            res = max(res,len(d))
        return res
