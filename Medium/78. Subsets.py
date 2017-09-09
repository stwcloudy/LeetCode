"""
解法一:
回溯递归 每个元素都有取 不取两种状态(非重复元素)
解法二:
总的子集数是2^n个,所以可以利用0-(2^n-1)的数来表示每个子集的状态
其中二进制位为1则表示对应位置的元素取,否则即不取
解法2不用判断空的情况
"""
###Solution1
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [nums]
        res = []
        def dfs(nums,sub,res):
            res.append(sub)
            for i in range(len(nums)):
                dfs(nums[i+1:],sub+[nums[i]],res)
        dfs(nums,[],res)
        return res

###Solution2
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        tot = 1<<n
        res = []
        for i in range(tot):
            sub,sta,bt = [],i,0
            while sta:
                if sta & 1:
                    sub.append(nums[bt])
                sta >>= 1
                bt += 1
            res.append(sub)
        return res
        