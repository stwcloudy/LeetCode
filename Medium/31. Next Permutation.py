"""
思路:
求按字典序的全排列的下一个,方法：
1.从序列末尾开始往前找,找到下标k 满足 nums[k] < nums[k+1],
若k = -1表明序列是降序排列,直接反转回升序.
2.继续从序列末尾开始找第一个大于nums[k]的数的下标l nums[l] > nums[k],交换这两个数的位置
3.将k之后的数组(注意这部分的序列是降序排列的)反转之后就得到了下一个排列
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i == -1:
            nums.reverse()
            return
        for j  in range(len(nums) -1,i,-1):
            if nums[j] > nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                break
        nums[i+1:] = nums[len(nums)-1:i:-1]
        