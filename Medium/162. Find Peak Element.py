"""
根据峰值的特点可以进行二分查找
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        l,r = 0,len(nums)-1
        while l < r:
            mid = (l+r)>>1
            if nums[mid] > nums[mid+1]:
                r = mid
            elif nums[mid] < nums[mid+1]:
                l = mid + 1
        return l
        