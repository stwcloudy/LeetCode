"""
先对数组排序之后深搜
注意每个数字可以重复使用

"""

class Solution(object):
    def search(self,candidates,target,sol,res):
        if target == 0:
            res.append(sol)
            return
        if target < 0:
            return 
        for i in range(len(candidates)):
            if target < candidates[i]:
                return
            self.search(candidates[i:],target-candidates[i],sol+[candidates[i]],res)
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        res = []
        self.search(candidates,target,[],res)
        return res
        