"""
思路:
本题的关键在于找到处于谷底的rating,以它为中心可以往两边扩展,我们知道每个人所得糖果数
只与他旁边两个的ratings相关,所以我们可以设置一个count数组记录每个人应得糖果数,初始化为1
那么：
1.先从左到右扫描,当前的rating的值比上一个大,则count[i]在count[i-1]基础上加1
2.再从右到左扫描,当前的rating比后一个大,此时由于之前扫描过一次更新过,所以要取两者的较大者
最后把所有的count[i]加起来就是结果,该算法的时间复杂度是O(n)，空间复杂度也是O(n)
-----------------------------------------------------------------------------------------------
简化空间复杂度:
初始先给第一个同学1个
对于一个同学,他所得到的糖果数有三种情况:
1.他的rating的值与上一个相等,则先分配1个给他
2.他的rating的值大于上一个,则分配prev+1个(prev表示的是上一个分配的糖果数)
3.他的rating值小于上一个,则此时不确定下降沿有多少个,所以用一个countDown变量记录下降沿有多少个,且保持prev不变
综合以上三种情况,可以在一遍扫描中得到最后答案
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        n = len(ratings)
        count = [1]*n
        res = 0
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                count[i] = count[i-1] + 1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                count[i] = max(count[i],count[i+1]+1)
        for i in range(n):
            res += count[i]
        return res

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        n = len(ratings)
        res,prev,countDown = 1,1,0
        for i in range(1,n):
            if ratings[i] >= ratings[i-1]:
                if countDown > 0:
                    res += (countDown)*(countDown+1)/2
                    if countDown >= prev:
                        res += countDown + 1 - prev
                    countDown = 0
                    prev = 1
                prev = 1 if ratings[i]==ratings[i-1] else prev + 1
                res += prev
            else:
                countDown += 1
        if countDown > 0:
            res += (countDown)*(countDown+1)/2
            if countDown >= prev:
                res += countDown + 1 - prev
        return res