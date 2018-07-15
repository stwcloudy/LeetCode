'''
每次将n-1个元素加1 相当于每次将一个元素减1
k = sum(nums) - n*min(nums)

与之类似还有462.Minimum Moves to Equal Array Elements II
'''
class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)*min(nums)
