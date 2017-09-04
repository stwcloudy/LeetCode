"""
朴素的解法就是枚举两边的柱子,复杂度为O(n^2)，会超时
双指针的题,还需要多加练习.
在discuss中看到一个关于O(n)解法的双指针正确性的证明：
  1 2 3 4 5 6
1 x ------- o
2 x x
3 x x x 
4 x x x x
5 x x x x x
6 x x x x x x
行列分别表示选取的左边界右边界的下标值,比如(1,6)表示左边界下标为1,右边界的下标为6
打叉的部分是不用考虑的(相等表示柱子重合,不合法,而下三角的结果和上三角处一样)
最开始我们选取(1,6),假设height[1] <= height[6],那么此时2,3,4,5的右边界就没有必要枚举
因为宽度变小而高度最多为height[1]的值,所以总面积一定变小的,所以此时应该左边界右移同理，当左边界
大于右边界时,也只需要左移右边界
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0,len(height) - 1
        res = 0
        while l < r:
            if height[l] <= height[r]:
                res = max(res,(r-l)*height[l])
                l += 1
            else:
                res = max(res,(r-l)*height[r])
                r -= 1
        return res