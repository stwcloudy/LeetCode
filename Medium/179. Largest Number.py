"""
给一个非负整数构成的list，要求组合出最大值的一个数
例：[3, 30, 34, 5, 9] -> 9534330
其实就是一个字符串排序的问题，给定任意两个字符串形式的数字，如'3','30' '3' + '30' > '30' + '3' 所以'3'应该在'30'前面
所以算法核心在于写一个cmp比较函数，在调用系统的排序方法进行排序即可，注意如果全为0的话只需输出‘0’
"""

class Solution:
	# @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
    	def compare(s1,s2):
    		_pre = s1 + s2
            _post = s2 + s1
            if s1 > s2 :
            	return 1
            elif s1 < s2 :
            	return -1
            else:
            	return 0
        l = [str(num) for num in nums]
        l.sort(lambda x,y : compare(x,y))
        return ''.join(l).lstrip('0') or '0'