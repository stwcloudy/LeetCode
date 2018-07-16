'''
题意:n盏灯 初始状态都开着, 4个按钮,每个按钮的作用是:
1.Flip all the lights.
2.Flip lights with even numbers.
3.Flip lights with odd numbers.
4.Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
现有m次操作,求m次之后一共有多少种不同的状态

讲得比较详细的一个post
https://leetcode.com/problems/bulb-switcher-ii/discuss/107266/Lazy-generalizable-O(1)-python-solution-with-explanation
大意是对于灯来说,四种操作都有作用,不作用两种选择, 所以一共2^4=16种状态，但是1等价于2+3 所以可以不要1 一共就是2^3=8种:
: {}
1: odd integers
2: even integers
1+2: all integers
3: integers n s.t. n%3==1
3+1 integers n s.t. n%3==1 and n%2==1
3+2: integers n s.t. n%3==1 and n%2==0
3+1+2: integers n s.t. n%3!=1

得到8种状态顶多需要3次操作,所以m = min(3,m), 而n=3是以上8种情况每个数字都能被影响到的最小数字，n>3的时候都是重复 所以n = min(n,3)
其他情况枚举就行
'''
class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            if m == 1:
                return 3
            return 4
        if n >= 3:
            if m == 1:
                return 4
            elif m == 2:
                return 7
            else:
                return 8