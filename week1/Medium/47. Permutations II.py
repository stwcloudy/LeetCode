"""
类似的题会写个总结,用回溯求解的集合的相关问题，包括(子集的求和,集合的全排列
,求子集,甚至回文子集的情况)
本题先将集合元素排序,然后抽取第一个元素时判断其跟它的前一个字符是否相等,若相等
直接跳过(去重)
"""

class Solution(object):
    def dfs(self,nums,sol,res):
        if len(nums) == 0:
            res.append(sol)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:],sol+[nums[i]],res)
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums and len(nums) == 1:
            return [nums]
        nums.sort()
        res = []
        self.dfs(nums,[],res)
        return res