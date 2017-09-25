"""
思路:
双指针的应用
用两个指针记录当前left,right 所在位置,再记录当前左半部分和右半部分的最大高度,
水槽所在的位置是一个中间低两边高的凹槽形状,所以left,right的作用是枚举两个边界，
先判断两个指针所在位置高度大小,
1.left较小,则其右边界至少有一个right的位置保证可以装上水(水不会在右侧流走),所以只需要判断其和左半部分最高值的关系即可,
若小于maxleft 说明其是属于一个凹槽的一部分,则两者高度差即为此处位置的储水量,否则更新maxleft
2.right较小,则移动right 其余情况判别类似
时间复杂度为O(n)
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxleft,maxright = 0,0
        l,r = 0,len(height) - 1
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < maxleft:
                    res += (maxleft - height[l])
                else:
                    maxleft = height[l]
                l += 1
            else:
                if height[r] < maxright:
                    res += (maxright - height[r])   
                else:
                    maxright = height[r]
                r -= 1
        return res