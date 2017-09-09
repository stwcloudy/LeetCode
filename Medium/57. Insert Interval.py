"""
思路一:直接遍历区间数组找与target区间有交集的两个区域 合并即可
思路二:二分分别查找左侧最后一个start值大于target的start的,右侧查找第一个end
值大于target的end值的区间,然后如果与target还有交集,则两个指针i,j分别再向两边移动
最后得到的结果就是包括到i区间的区间并上更新后的区间并上j之后的区间
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        n = len(intervals)
        def binarySearch(left,right,target,flag):
            while left <= right:
                mid = (left + right) >> 1
                m = intervals[mid].start if flag else intervals[mid].end
                if m < target:
                    left = mid + 1
                elif m > target:
                    right = mid - 1
                else:
                    return mid
            return right if flag else left
        i = binarySearch(0,n-1,newInterval.start,1)
        j = binarySearch(0,n-1,newInterval.end,0)
        if i >= 0 and intervals[i].end >= newInterval.start:
            newInterval.start = min(intervals[i].start,newInterval.start)
            i -= 1
        if j < n and intervals[j].start <= newInterval.end:
            newInterval.end = max(intervals[j].end,newInterval.end)
            j +=1
        return intervals[:i+1]+[newInterval]+intervals[j:]