"""
寻找翻转后的数组的最小值
思路:
1.如果当前left的值小于right的值说明此时left即为最小值 返回
2.只要存在翻转且nums[mid]在前半段 操作都是使left增加,而判断的条件就是nums[mid] > nums[right]
3.由于2的存在,所以right不会减到前半段,所以当nums[mid] <= nums[right]时,可以放心的right = mid
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0,len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left+right)>>1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]