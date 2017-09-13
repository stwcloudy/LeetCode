"""
思路:
这是在同学那请教来的思路,很巧妙的一种二分的应用,先说一下基本流程
首先不管分成多少parts,最大子数组和都有一个上界和下界,每个元素单独为一组时,最大为数组最大值记为maxnum
整个数组为一个组时,最大为整个数组和,记为arrsum,而我们所求的答案就在这个区间之内[maxnum,arrsum]
然后便是对答案的二分查找:
mid = (l+r)>>1
划分每个区间的和都不大于mid,则此时会出现两种情况:
1.划分到最后多于m个区间,说明此时的mid过小,调整下界l = mid + 1
2.少于或者刚好等于m个区间,说明尚有余地,因为求的是最小的和,所以r = mid -1
---------------------------------------------------------------------------------------------------------
算法正确性说明:
https://leetcode.com/problems/split-array-largest-sum/discuss/
当时是看了这篇文章才在理论上说服自己这个算法的正确性
按照文章的说法,我们可以这样想,不管你是划分为多少个区间,在m固定的情况下,我们所寻找的最大区间的最小值总是存在
不妨设为k,由于我们知道了答案的一个上下界[maxnum,arrsum],那我们知道,在区间[k,arrsum]之间的数,不管怎么划分
得到的区间数总是小于等于m,而对于[maxnum,k)之间的数,则其区间数总是大于m,相当于前半个区间不满足条件,而后半部分满足
这就是一个[0,0,0,...,0,1,1,1,,1...]的一个二元值的升序序列,我们的目标是查找第一个为1的地方,自然而然二分查找便能成功
所以算法到最后一定找到的是我们所求的答案

---------------------------------------

解法二:
dp[s][j]表示arr[j],arr[j+1],...,arr[n-1]中划分为s个区间的最小最大值
则dp[s+1][i] = min(max(dp[s][j],arr[i]+arr[i+1]+...+arr[j-1])) 其中i+1 <= j <= n-s
该方法的复杂度比二分高 但是适用于数组中有负数的情况
"""


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        maxnum = nums[0]
        arrsum = nums[0]
        for num in nums[1:]:
            maxnum = max(maxnum,num)
            arrsum += num
        def judge(nums,m,target):
            cnt = 1
            tmpsum = 0
            for num in nums:
                tmpsum += num
                if tmpsum > target:
                    cnt += 1
                    tmpsum = num ##每个区间严格小于等于target
                    if cnt > m:
                        return False
            return True
        l,r = maxnum,arrsum
        while l <= r:
            mid = (l+r)>>1
            if judge(nums,m,mid):
                r = mid - 1
            else:
                l = mid + 1
        return int(l)

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        arrsum = [0]*(n+1)
        for i in range(1,n+1):
            arrsum[i] = arrsum[i-1] + nums[i-1]
        dp = [0]*n
        for i in range(n):
            dp[i] = arrsum[n] - arrsum[i]  ##不分段时候的初值
        import sys
        for s in range(1,m):
            for i in range(n - s):
                dp[i] = sys.maxsize
                for j in range(i+1,n-s+1):
                    tmp = max(arrsum[j] - arrsum[i],dp[j])
                    if tmp <= dp[i]:
                        dp[i] = tmp
                    else:
                        break
        return dp[0]
        