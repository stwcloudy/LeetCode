'''
题意:两个长度相同的数组A,B, 可以调整A的顺序,返回满足A[i] > B[i]个数最多的排列
解法1:
1. 先将两个数组升序排序
2. 对每个位置来说, A[i] > B[i] 则处理下一个位置，否则, 找到B[i]在A中第一个大于的位置,在A中将此位置前的元素都翻转到数组最后，贪心的将最小的A抵消最大的B
例子:
A=[8,12,24,32], B=[11,13,25,32]
8<11 A 调整为A=[12,24,32,8]
最后结果调整回以前B中的顺序即可

解法2:
也是贪心的思想,B按逆序排列，对当前最大的B来说,如果A中最大的值大于他，则该位置即为当前A，否则用最小的A中元素对应
'''
解法1:
class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)
        B = sorted((B[i],i) for i in range(len(A)))
        n = len(A)
        ans, rev = [],[]
        i = 0
        j = 0
        while i < n and j < n:
            if A[i] > B[j][0]:
                ans.append(A[i])
                j += 1
            else:
                rev.insert(0,A[i])
            i += 1
        ans += rev
        ret = [0]*n
        for i in range(n):
            ret[B[i][1]] = ans[i]
        return ret
        
解法2:
class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)
        heap = []
        n = len(A)
        ans = [0]*n
        for i, num in enumerate(B):
            heapq.heappush(heap, (-num,i))
        l, r = 0, n - 1
        while heap:
            num, idx = heapq.heappop(heap)
            if A[r] > -num:
                ans[idx] = A[r]
                r -= 1
            else:
                ans[idx] = A[l]
                l += 1
        return ans
