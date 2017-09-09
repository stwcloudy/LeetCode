"""
思路:
原本我以为加上有重复数字之后需要判断两个边界的大小关系，所以情况会复杂得多,
但是后来想到,不管他是否有重复数字,序列的两个部分还是分别递增,且nums[0]>=nums[n-1]
我们在第一个题中的思路就是找一个递增的序列,判断target是否在这个区间,这里可以做一样的工作,
只是把nums[mid]>=nums[l]中的等号摘出去,只有当nums[mid]严格大于nums[l],它们两所在的区间才算是递增区间(即便其中可能有相同的)
这样一来思路还是没变,如果在这个区间中,就把right = mid - 1,否则left = mid + 1
同理,nums[mid]严格小于nums[l]时,nums[mid]-nums[r]也是一个递增区间
最后再判断nums[mid] == nums[l]的情况.此时不能确定区间是否递增,则将l+1向前移一步.
该算法平均情况下是O(logn),但是最坏情况下会退化到O(n)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)>>1
            if nums[mid] == target:
                return True
            if nums[mid] > nums[l]:
                if target < nums[mid] and nums[l]<= target:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False