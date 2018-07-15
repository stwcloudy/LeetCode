'''
题意: 求出数组中最长递增子序列的个数
对应求最长递增子序列长度两种方法， 1.dp[i] 存 到i为止的最长递增长度.2dp[i]存到i为止的最长子序列
此题用第二种方法，再增加一个counts数组counts[i]表示长度为i的子序列的结尾数字,最后结果就是counts最后一个列表的长度

'''
class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        res = 0
        seq = []
        counts = []
        for num in nums:
            pos = bisect.bisect_left(seq, num)
            if pos < len(seq):
                seq[pos] = num
            else:
                seq.append(num)
                counts.append([])
            repeats = bisect.bisect_right(counts[pos-1], num) if pos > 0 else 1
            counts[pos].extend([num]*repeats)
        return len(counts[-1]) if counts else 0