"""
思路：
类比两个数和的情况,先将数组排序之后,枚举第一个数，剩下的两个数在余下的数组里找
设置头尾指针在余下数组中,通过当前三个数和的情况移动左右指针,注意处理重复情况和几个tips
1.由于数组已经排序,所以当某个数已经大于0之后就直接break
2.当前枚举的数与前一个相同,跳过本轮循环(因为结果与上一个一样)
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i + 1,len(nums)-1
            while l < r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l+1] == nums[l]: #去重
                        l += 1
                    while l < r and nums[r] == nums[r-1]: #去重
                        r -= 1
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return res