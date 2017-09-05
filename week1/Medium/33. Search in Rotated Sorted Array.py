"""
这题比之后有重复数字的稍微简单一点,由于序列极具特征,序列分为两段分别都是升序,且
第一段的最小的数都比第二段中最大的大,所以依旧可以用二分查找的思想在里边.
mid = (l+r) >>1
1.若nums[mid] == target:直接返回mid
2.由于序列中不存在重复数字,所以可以利用nums[mid]和nums[l]或nums[r]的关系判断它所在区域,以nums[l]为例
    2.1 若nums[mid] >= nums[l],说明要么mid == l 要么 nums[mid]在第一段中,此时判断target与nums[mid]的关系
    如果target处于nums[l],nums[mid]之间,则r = mid-1 在此区间寻找,否则在另一个区间寻找
    2.2 否则,mid的值比l大却nums[mid] < nums[l] 其职能出现在第二段,此时若target在nums[mid],nums[r]之间,l = mid +1
3.由于循环结束条件是l>r,所以若target存在序列中,循环中一定能返回,所以循环结束后可直接返回-1未找到
有重复数字出现的情况稍微复杂一点 之后会在那题中有详细说明
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)>>1
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1