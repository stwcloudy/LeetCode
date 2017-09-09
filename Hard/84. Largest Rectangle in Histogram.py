"""
思路:
动态规划,将每一个位置处的左边界和右边界分别确定下来,最后求每个边界处的矩形的最大面积即可
left[i],right[i]分别表示i处的左边界和右边界
求left[i]时,判断：
heights[left[i]-1] >= height[i] 就更新left[i]
right[i]同理
解法二:
用一个栈存储高度递增序列的下标,当前位置的高度小于栈顶下标对应的高度,说明以height[st.top()]为高度的
矩形的右边界找到,计算它的面积然后更新最大面积
为了避免判断特殊情况只有一个或没有的情况在heights数组的头尾分别加了一个高为0的高度

"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left = [i for i in range(n)]
        right = [i for i in range(n)]
        for i in range(1,n):
            while left[i] > 0 and heights[left[i]-1] >= heights[i]:
                left[i] = left[left[i]-1]
        for i in range(n-2,-1,-1):
            while right[i] < n-1 and heights[right[i]+1] >= heights[i]:
                right[i] = right[right[i]+1]
        maxarea = 0
        for i in range(n):
            maxarea = max(maxarea,(right[i]-left[i] + 1)*heights[i])
        return maxarea

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.insert(0,0)
        heights.append(0)
        n = len(heights)
        st = []
        maxarea = 0
        st.append(0)
        for i in range(1,n):
            while heights[i] < heights[st[-1]]:
                idx = st[-1]
                st.pop()
                maxarea = max(maxarea,heights[idx]*(i - (st[-1] + 1)))
            st.append(i)
        return maxarea
        
        