"""
先将区间start升序排序
用一个结果列表存储结果,如果当前res为空或者当前列表中最后一个区间的end值小于当前
遍历到的区间的start值,则直接添加当前区间
否则,更改res[-1]的end为其中较大者
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        res = []
        for i in intervals:
            if res and res[-1].end >= i.start:
                res[-1].end = max(res[-1].end,i.end)
            else:
                res.append(i)
        return res
        