"""
思路:
排序之后按0,1,2放置,所以可以用两个指针一个指向0当前第一个不为0的位置
一个指向自右向左第一个不为2的位置
从第一个位置遍历数组 碰见0 则与pos0所在位置数字交换
碰见2则与pos2所在位置交换(这里要注意交换后i的位置不能动,因为可能交换过来的是0 还得在交换一次)
思路2:
这是看见的别人的代码,非常巧妙,设置三个指针 前移的速度2>1>0
这样每次都是正确的值会覆盖之前的值
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos0,pos2 = 0,len(nums)-1
        i = pos0
        while i <= pos2:
            if nums[i] == 2:
                nums[i],nums[pos2] = nums[pos2],nums[i]
                pos2 -= 1
                i -= 1
            elif nums[i] == 0:
                nums[i],nums[pos0] = nums[pos0],nums[i]
                pos0 += 1
            i += 1


            class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pivot0,pivot1,pivot2 = -1,-1,-1
        for i in range(len(nums)):
            if nums[i] == 0:
                pivot2 += 1
                nums[pivot2] = 2
                pivot1 += 1
                nums[pivot1] = 1
                pivot0 += 1
                nums[pivot0] = 0
            elif nums[i] == 1:
                pivot2 += 1
                nums[pivot2] = 2
                pivot1 += 1
                nums[pivot1] = 1
            else:
                pivot2 += 1
                nums[pivot2] = 2