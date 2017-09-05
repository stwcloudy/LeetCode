"""
思路:
求在一个大小为n的数列中,第一个没出现的正整数(不包括0)
所以一种比较巧妙的方式数列一共n个位置,当1-n的数都在时,不存在的数就是n+1
所以可以将出现的数都放到他应该在的位置,比如3放在nums[2](数组以0开始)的位置
比如[3,4,-1,1]
1. 3应该在的位置nums[2]=-1 所以将3换到-1的位置[-1,4,3,1]
2.再判断4 [-1,1,3,4]
3.由于nums[1-1] = -1 != 1 ,继续交换[1,-1,3,4]
4.3,4的位置正确,所以交换完毕
最后遍历数组 谁不在位置,所求结果就是它
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i = 0
        n = len(nums)
        while i < n:
            idx = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and idx + 1 != nums[idx]:
                    nums[i],nums[idx] = nums[idx],nums[i]
            else:
                i += 1
        for i in range(n):
            if i + 1 != nums[i]:
                return i+1
        return n+1
                    