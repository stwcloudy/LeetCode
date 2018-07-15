'''
该题每次对一个数加1或减1，最后求最小的步数到所有数相同
先将该数组排序，假设最后的数字为k, 如果k在排序后到数组中的位置靠前，增加k， <=k的数字都会增加一步, >=k的数字都会减少一步,
所以应该尽量让两侧数字增加减少的步数一致 ，中位数
'''
class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        res = 0
        target = nums[len(nums)//2]
        for num in nums:
            res += abs(num-target)
        return res