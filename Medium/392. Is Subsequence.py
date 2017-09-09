"""
双指针,找到t中字符即移动t的指针,s指针一直往前移动
解法2：
用一个字典存储t中每个字符出现的下标(升序)
然后遍历s中的字符二分查找第一个大于当前index的下标位置,如果没找到 返回false

"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        m,n = len(s),len(t)
        dp = [False]*(m+1)
        i,j = 0,0
        while j < n:
            if t[j] == s[i]:
                i += 1
                if i == m:
                    return True
            j += 1
        return False

###解法2：
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        m,n = len(s),len(t)
        d = {}
        for i,ch in enumerate(t):
            if ch not in d:
                d[ch] = [i]
            else:
                d[ch].append(i)
        def binary_search(nums,target):
            l,r = 0,len(nums)-1
            while l <= r:
                mid = (l+r)>>1
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1 if l >= len(nums) else nums[l]
        idx = -1
        for i in range(len(s)):
            if s[i] not in d:
                return False
            idx = binary_search(d[s[i]],idx)
            if idx == -1:
                return False
        return True