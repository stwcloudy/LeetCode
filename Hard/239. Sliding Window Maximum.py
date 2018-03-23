"""
暴力方法时间复杂度O(NK),外层循环枚举窗口起始点,内层循环遍历窗口找最大值
第二种线性时间复杂度的方法是使用deque双向队列,队列大小最多为k,队列中的元素都是当下及以后
有可能成为最大值的元素的下标
举个例子:
[2,1,3,4,6,3,8,9,10,12,56]
q = [2]
1到达1 < 2 入队 q = [2,1]
3到达3 > 1 1出队,2 < 3 2出队 q = [3](3比1,2都大,1,2不可能成为最大值所以直接出队)以下类似
为了保证队列中的数字都在当前窗口中,我们存的时候存的是下标,这样当存的下标j <= i - k (k<=i<n)队首出队
最后剩下在队列中的都是当前第一大的数,第二大的数,第三大的数,...
由于数组中的每个数最多进队一次 出队一次 所以总的时间复杂度是O(n)
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 1:
            return nums
        win = []
        for i in range(k):
            while win and nums[win[-1]] < nums[i]:
                win.pop()
            win.append(i)
        res = []
        for i in range(k,len(nums)):
            res.append(nums[win[0]])
            while win and win[0] <= i - k:
                win.pop(0)
            while win and nums[win[-1]] < nums[i]:
                win.pop()
            win.append(i)
        res.append(nums[win[0]])
        return res