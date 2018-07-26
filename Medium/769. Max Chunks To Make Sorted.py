'''
给定一个数组,数组中的数都是0-n-1, n为数组长度,要求找出最多的chunk,将每个chunk中的元素排序之后
concatenate起来是一个排序数组
思路:
由于数字大小都在0-n-1, 每一个chunk中的最大值,都必须满足到当前窗口的下标,即如果当前最大值等于下标，就找到一个chunk
2,1,4,0,3,5
两个chunk [2,1,4,0,3] [5]
'''
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        curmax = -1
        chunk = 0
        for i, num in enumerate(arr):
            curmax = max(curmax, num)
            if curmax == i:
                chunk += 1
        return chunk
        