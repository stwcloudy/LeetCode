"""
思路:
按照重复2次的题的思路,可以将每个数的二进制位数单独分开来看,我们知道只有一个数出现了一次而其他数都出现了3次
所以对于某一个二进制位来说只有两种情况:
1.该位为1的个数是3的倍数,则表示所求的数在该位为0
2.为1的个数是3的倍数+1,则表示所求的数在该位为1
这样将每一位的0,1表示求出来 就是最后的答案
--------------------------------------------------
解法二和解法一的思路是类似的,但是采用了三个变量来记录的形式
ones,twos,threes分别表示截止目前为止的数的各个二进制位上出现1的次数分别为1,2,3(模3之后的结果)
的数位,当ones,twos其中某一位都为1时表示该位出现了3次,需要清零计算

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            mask = (1 << i)
            cnt = 0
            for num in nums:
                if num & mask:
                    cnt += 1
            rem = cnt % 3
            if rem != 0:
                if i == 31:
                    res -= mask
                else:
                    res |= mask
        return res

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones,twos,threes = 0,0,0
        for num in nums:
            twos |= (ones&num)
            ones ^= num
            threes = ~(ones&twos)
            ones = ones&threes
            twos = twos&threes
        return ones