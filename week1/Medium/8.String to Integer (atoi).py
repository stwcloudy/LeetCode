"""
注意判断各种情况：
1.注意处理前后空格字符的问题
2.处理之后的字符串首字符为'+','-'的情况
3.经测试后发现,对包含非数字字符的情况返回值是截断之前得到的数字
4.处理越界的问题
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if not str:
            return 0
        str = str.strip()
        ans = 0
        flag = 1
        i = 0
        if str[0] == '-' or str[0] == '+':
            if str[0] == '-':
                flag = -1
            i += 1
        while i < len(str):
            if str[i] >= '0' and str[i] <= '9':
                if ans > INT_MAX/10 or (ans == INT_MAX/10 and int(str[i]) > 7):
                    if flag == 1:
                        return INT_MAX
                    else:
                        return INT_MIN
                ans = ans * 10 + int(str[i])
            else:
                break
            i += 1
        return flag*ans