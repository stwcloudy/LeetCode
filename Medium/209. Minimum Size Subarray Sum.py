"""
本题是给定一个全是正数的数组nums[]和一个目标值s,要求找出子区间和大于等于s的最小区间长度，
如果不存在(所有序列和加起来都小于s 返回0)
边界情况：
数组为空或者数组所有数字加起来都小于s 此时返回0

O(N)的做法：
用双指针，left,right分别指向当前大于等于目标值的区间的左边界和右边界，每次相应移动left和right来求得最小区间，
具体做法，先初始化left，right = 0，0：
1. 当sum(nums[:right]) < s时，right += 1
2. 当sum(nums[:right]) >= s  left += 1
3. minlen = min(minlen,right - left + 1)

O(NlogN)做法：
由于数组所有数字为非负数字，所以子数组和是一个单调上升序列，可以用上二分查找的东西。
举个例子 nums = [2, 3, 1, 2, 4, 3], sums = [0,2,5,6,8,12,15]
对于sums中每个大于s的右边界，我们用二分查找找到sums中第一个大于sums[i] - s 的位置，表明在原nums中该对应位置到i边界的和刚好大于等于s
如 sums[5] = 12,要找第一个大于12-7 = 5 的数字，即为sums[3] = 6，原数组中[1,2,4] 加起来刚好为7
"""
import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0,0
        subsum = 0
        if not nums:
            return 0
        n = len(nums)
        res = sys.maxint
        while right < n :
            while right < n and subsum < s:
                subsum += nums[right]
                right += 1
            if subsum < s:
                break
            while left <= right and subsum >= s:
                subsum -= nums[left]
                left += 1
            res = min(res,right - left + 1)
        return 0 if res == sys.maxint else res


import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(left,right,arr,target):
            while left < right:
                mid = (left + right) / 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return right if arr[right] > target else -1
        if not nums:
            return 0
        n = len(nums)
        sums = [0] * (n + 1)
        minlen = sys.maxint
        for i in range(1,n+1):
            sums[i] = sums[i-1] + nums[i-1]
        print sums
        for i in range(1,n + 1):
            if sums[i] >= s:
                print sums[i]
                pos = binarySearch(0,i,sums,sums[i] - s)
                print pos
                if pos != -1:
                    minlen = min(minlen, i - pos + 1)
                    
        return minlen if minlen != sys.maxint else 0

