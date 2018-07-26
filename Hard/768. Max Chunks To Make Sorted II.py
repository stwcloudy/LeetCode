'''
与769一样,但是数组中的数组不在连续,可能很大,而且有重复数字.
解法1:
依托于769,可以将问题转化为769中的问题,将原数组中的数字离散化,保持相对大小，对数组中的(num,index)元组排序
则排序之后index数组就可以表示其在原数组中的相对大小,此时直接对index数组做769中的操作即可
解法2:
用一个栈来维持当前的trunk,栈中的值是元组(t_min,t_max)表示该trunk中的最大值和最小值,遍历数组
每次将当前(num,num)与栈顶元素比较,若比t_max还大,将其作为一个独立的trunk插入堆栈,否则合并栈顶的trunk直至t_max <= cur_min
'''
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        st = []
        for num in arr:
            ele = [num,num]
            while st and st[-1][1] > ele[0]:
                top = st.pop()
                ele[0] = min(ele[0], top[0])
                ele[1] = max(ele[1], top[1])
            st.append(ele)
        return len(st)