'''
给定一个字符串,重新排列字符串中的字符判断是否能够任意相邻两个字符不相同,不能就返回'',可以就返回任意一个合法串
解法:
先统计每个字符出现的次数,对于出现次数最多的字符,如果其出现次数>=(n+1)/2 + 1,n为字符串长度,则不能满足条件直接返回空字符串.
否则,就能够将其重排,选择的排法是,将字符按照其重复次数放入大顶堆,每次取出最多的一个元素和次多的元素交叉,直到堆为空
'''
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        ch_count = collections.defaultdict(int)
        for ch in S:
            ch_count[ch] += 1
        if max(ch_count.values()) >= (n+1) // 2 + 1:
            return ''
        heap = []
        for k, v in ch_count.items():
            heapq.heappush(heap,(-v,k))
        ans = ''
        while heap:
            tup1 = heapq.heappop(heap)
            if heap:
                tup2 = heapq.heappop(heap)
                ans += tup1[1] + tup2[1]
                if tup1[0] + 1 < 0:
                    heapq.heappush(heap,(tup1[0]+1, tup1[1]))
                if tup2[0] + 1 < 0:
                    heapq.heappush(heap,(tup2[0]+1, tup2[1]))
            else:
                ans += tup1[1]
        return ans