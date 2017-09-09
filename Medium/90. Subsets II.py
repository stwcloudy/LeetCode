"""
通过排序之后检验前后两个数字是否相同来去重 
其他类似 dfs 回溯
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [nums]
        res = []
        nums.sort()
        def dfs(nums,sub,res):
            res.append(sub)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:],sub+[nums[i]],res)
        dfs(nums,[],res)
        return res