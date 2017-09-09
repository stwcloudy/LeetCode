"""
水题
思路：
将数组排序之后，用两个指针分别指向数组的头尾，判断nums[left]+nums[right] == target
< left++
> right--
由于数据保证只有一组解，找到相等时再在原数组中找下标即可

法二：
也可以用一个dict来存储(val,index) O(n)时间
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        op_nums = sorted(nums) #sorted函数会return新的list
        l,r = 0,len(nums) - 1
        while l < r:
        	add = op_nums[l] + op_nums[r]
        	if add == target:
        		break
        	elif add < target:
        		l += 1
        	else:
        		r -= 1
        for i in range(len(nums)):
        	if nums[i] == op_nums[l] or nums[i] == op_nums[r]:
        		res.append(i)
        return res

