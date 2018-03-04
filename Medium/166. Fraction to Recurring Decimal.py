"""
本题算法比较简单 但是考量的是细心程度和对边界情况的考虑
需要将几点考虑进去：
1. 正负数的情况
2. 分子是0的情况
3. 不循环和循环的表示方法不相同，且循环的只是将循环节标注(用括号)起来
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        repeat = False
        res = ''
        if numerator == 0:
            return '0'
        res += '-' if ((numerator > 0) ^ (denominator > 0)) else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        res  += str(numerator // denominator)
        remain = numerator % denominator
        if remain == 0:
            return res
        res += '.'
        rep_map = {} #用于匹配(除数，结果长度)当除数重复时，表示开始循环
        while remain != 0:
            remain *= 10
            if remain in rep_map:
                rep_idx = rep_map[remain] - 1
                res = res[:rep_idx] + '(' + res[rep_idx:] + ')'
                break
            res += str(remain // denominator)
            rep_map[remain] = len(res)
            remain = remain % denominator
        return res