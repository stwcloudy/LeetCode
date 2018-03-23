"""
只有两个数字只出现了一次,那所有数xor之后的结果是res1^res2,且非零,所以我们可以取最后这个结果中
某个为1的位(方便起见直接(tmp&(-tmp))取最右的1),该位置为1表示结果中的两个数只有一个在该位置为1,
然后就把整个数组分为两个部分,在该位置上为1或者0,分别在这两个集合上取异或,得到两个结果
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 0
        for num in nums:
            tmp ^= num
        rmbit = tmp&(-tmp)
        res1,res2=0,0
        for num in nums:
            if num & rmbit:
                res1 ^= num
            else:
                res2 ^= num
        return [res1,res2]