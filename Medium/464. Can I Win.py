"""
由于最大选择的数的上限是20 我们可以用一个bits位表示哪个数字选中
从而将信息存储下来 采用自上而下的带备忘录的搜索寻找
"""

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= maxChoosableInteger:
            return True
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        from collections import defaultdict
        m = defaultdict(bool)
        def helper(target,bits):
            if bits in m:
                return m[bits]
            for i in range(1,maxChoosableInteger+1):
                rm = (1<<i)
                if (rm&bits == 0) and (i >= target or helper(target - i,bits|rm) == False):
                    m[bits] = True
                    return True
            m[bits] = False
            return False
        return helper(desiredTotal,0)