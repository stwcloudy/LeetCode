"""
深搜递归构造解,分别以nums中的每一个元素为开头+剩余所有元素的全排列构造解
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 1:
            return [nums]
        res = []
        def dfs(per,nums):
            if len(nums) == 0:
                print per
                res.append(per)
                return
            for i in range(len(nums)):
                dfs(per+[nums[i]],nums[:i]+nums[i+1:])
        dfs([],nums)
        return res