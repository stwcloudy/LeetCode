"""
思路:
数组能够划分为两个和相等的子数组,说明整个数组的和一定是偶数,奇数的情况不可能
再把tot/2就把问题转化为求数组中是否有子数组的和==tot/2
这就是之前的子集和的问题,将数组排序之后,去重剪枝即可

解法2:
初始化的思路一致,还是转化为求数组中子数组和为target=tot/2的问题
由于每个数组中元素只能用一次,且是要求恰好等于target,这不就是个0-1背包问题
时间复杂度O(n*target) 空间复杂度O(target)

解法3:
discuss中看到的大神的思路,类似dp[i] 用bits[i]中第i位为1表示i能由数组求和得到
A tiny example, nums=[2, 3, 5], initial bits is 1, traversing through nums
when num=2, bits=101, which represents nums can sum to 0 and 2
when num=3, bits=101101, which represents nums can sum to 0, 2, 3, 5
when num=5, bits=10110101101, which represents nums can sum to 0, 2, 3, 5, 7, 8, 10
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        if len(nums) == 1:
            return False
        nums.sort()
        tot = sum(nums)
        if tot & 1:
            return False
        target = tot // 2
        dp = [False]*(target+1)
        dp[0] = True
        def dfs(nums,target):
            if target < 0:
                return False
            if target == 0:
                return True
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    return False
                if dfs(nums[i+1:],target-nums[i]):
                    return True
            return False
        return dfs(nums,target)
###动态规划求解
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        if len(nums) == 1:
            return False
        tot = sum(nums)
        if tot & 1:
            return False
        target = tot // 2
        dp = [False]*(target+1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] = dp[j] or dp[j-nums[i]]
        return dp[target]

###bits wise
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        if len(nums) == 1:
            return False
        tot = sum(nums)
        target = tot // 2
        bits = 1
        for n in nums:
            bits |= bits<<n
        return (not tot%2==1) and ((bits>>target)&1 == 1)