"""
思路:
与153题类似 多了个重复性,再把小于等于的情况分离出来即可,等于时表面不可判断,让r-1
不影响结果
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l+r) >>1
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]
        