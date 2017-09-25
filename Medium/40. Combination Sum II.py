    """
与上一题一样的思路,只是这题不容许有重复使用一个数字的情况
所以搜索的时候每次都向前搜索,且为了避免出现相同的结果,先将数组排序之后,如果当前数字和前一个相同
就不必判断当前的数字的情况(因为在之前已经判断过了)
"""

class Solution(object):
    def dfs(self,nums,target,sol,res):
        if target < 0:
            return
        if target == 0:
            res.append(sol)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if target < nums[i]:
                return
            self.dfs(nums[i+1:],target-nums[i],sol+[nums[i]],res)
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        res = []
        self.dfs(candidates,target,[],res)
        return res