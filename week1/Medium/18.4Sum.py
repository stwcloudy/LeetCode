"""
思路：
接连遇到2Sum,3Sum,4Sum,希望写个通用的Nsum的版本n
用递归+剪枝来做,由于剪枝的工作存在,该方案的运行时间很快
剪枝：
1.类似之前一样先将数组排序之后,如果存在target < n * nums[i] or target > n*nums[-1]的情况
说明这之后都不会有结果出现,直接break。
2.同样要去除重复结果
基础返回条件：
n==2的时候就用当前数组做2Sum的运算,一旦有匹配的,直接加入结果中
"""

class Solution(object):
    def helper(self,nums,target,n,ele,res):
        if n == 2:
            l,r = 0,len(nums) - 1
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp == target:
                    res.append(ele + [nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif tmp < target:
                    l += 1
                else:
                    r -= 1
            return
        for i in range(len(nums)-n+1):
            if target < n * nums[i] or target > n*nums[-1]:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            self.helper(nums[i+1:],target-nums[i],n-1,ele+[nums[i]],res)
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        self.helper(nums,target,4,[],res)
        return res
        
        