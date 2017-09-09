"""
思路:
我的想法是找到一个窗口,left,right边界分别代表下标最大的小于target的位置和下标最小的大于target的值
如[7,8,9] target=8 返回的left=0,right = 2
这样的话若left+1 == right说明没有相应的target 返回[-1,-1],否则返回[left+1,right-1]
而寻找left,right的过程则用二分查找的方法,找边界的时候细节略微不同:
left:寻找left时,nums[mid]==target 右边界减少
right:寻找right时,nums[mid] == target 左边界增加
其余都与二分查找一样
最后返回值时,找left，返回的是最终的右边界,right是返回左边界
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        def find(left,right,flag):
            while left <= right:
                mid = (left+right)>>1
                if flag:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            return right if flag else left
        n = len(nums)
        l,r = find(0,n-1,1),find(0,n-1,0)
        print l,r
        if l + 1 == r:
            return [-1,-1]
        else:
            return [l+1,r-1]