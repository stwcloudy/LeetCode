"""
与上题一样的思路,只不过把0换成了target,每次都判断当前最接近的数
一旦有相等的数立刻返回即可
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        diff = 0x7fff
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == target:
                    return target
                elif sum3 < target:
                    l += 1
                else:
                    r -= 1
                if abs(sum3 - target) < diff:
                    diff = abs(sum3 - target)
                    res = sum3
        return res