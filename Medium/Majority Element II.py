"""
本题是求数组中超过一半的数的扩展,思路一样,只是超过n/3的数最多可能为2个
所以要用两个候选者,当三个数都不一样的时候,删除这三个不影响最终结果,最后再扫描一遍确认是否是满足条件即可
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candi1,candi2 = 0,0
        times1,times2 = 0,0
        for num in nums:
            if candi1 == num:
                times1 += 1
            elif candi2 == num:
                times2 += 1
            elif times1 == 0:
                candi1 = num
                times1 = 1
            elif times2 == 0:
                candi2 = num
                times2 = 1
            else:
                times1 -= 1
                times2 -= 1
        res = []
        times1,times2 = 0,0
        for num in nums:
            if num == candi1:
                times1 += 1
            elif num == candi2:
                times2 += 1
        if times1 > len(nums)/3:
            res.append(candi1)
        if times2 > len(nums)/3:
            res.append(candi2)
        return res