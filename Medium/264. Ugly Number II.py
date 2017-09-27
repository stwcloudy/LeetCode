"""
思路:
要求第n个丑数,，每个丑数都是由2,3,5的因子构成,求第n个丑数时,必定是由前面n-1个丑数中
乘以2,3,5大于n-1个丑数中的最小者,由于题目中n最大为1690,所以可以先离线把所有1690个丑数计算出
最后直接O(1)读取即可,分别用t2,t3,t5表示乘2,3,5之后刚好大于当前丑数的下标,则下一个下标就是由
min(uglyNum[t2]*2,uglyNum[t3]*3,uglyNum[t5]*5)中生成
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglyNum = [0]*2000
        def getUglyNum(uglyNum):
            uglyNum[0] = 1
            t2,t3,t5=0,0,0
            idx = 0
            while idx < len(uglyNum) - 1:
                cur_num = min(uglyNum[t2]*2,uglyNum[t3]*3,uglyNum[t5]*5)
                idx += 1
                uglyNum[idx] = cur_num
                while uglyNum[t2] * 2 == cur_num:
                    t2 += 1
                while uglyNum[t3] * 3 == cur_num:
                    t3 += 1
                while uglyNum[t5] * 5 == cur_num:
                    t5 += 1
            return uglyNum
        uglyNum = getUglyNum(uglyNum)
        return uglyNum[n-1]