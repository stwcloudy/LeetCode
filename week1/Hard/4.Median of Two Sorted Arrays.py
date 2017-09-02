"""
法一:
该方法参考https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/
中位数的定义是指将一个序列分为两个部分，两部分长度相等且其中一部分的最大值小于另一部分的最小值，即：
len(nums[0...i-1]) == len(nums[i...m-1]) and max(left(nums)) <= min(right(nums))
所以要求中位数即求满足上诉条件的值即可，同理，两个序列时，也不需要将其全部排列有序之后寻找：
left               right
nums1[0...i-1]     nums1[i...m-1]
nums2[0...j-1]     nums2[j...n-1]
必须满足：
1.len(left) == len(right) i.e. i + j == n + m - i - j (or n + m -i -j + 1:当两个加起来是奇数的情况，左边会多1)
2.nums2[j-1] <= nums1[i] and nums1[i-1]<=nums2[j](这里先假设i,j的取值都不是边界，边界情况下面讨论)

所以该方法就只需要枚举每一个i(0<=i<=m) 找出对应的j=(n+m+1)/2 - i(所以为了保证j非负, m <= n,大于时交换序列即可)
判断2中不等式的关系来调整i,j的值：
1.满足不等式，找到i 可停止查找
2.nums2[j-1] > nums1[i],此时说明i过小，需将i右移,同时j会左移;
3.nums1[i-1] > nums2[j],此时说明i较大，需将i左移，同时j会右移
--------------------------------------------------------------
边界条件：i==0,i==m,j==0,j==n
我们发现,i==0时,nums1[i-1]非法,此时只需判断nums2[j-1]和nums1[i]的关系
同理,i == m 判断nums1[i-1]和nums2[j]的关系

最后求中位数时,若m+n 是奇数,则取max(nums1[i-1],nums2[j-1]),
偶数取(max(nums1[i-1],nums2[j-1]) + min(nums1[i],nums2[j]))/2
该算法是以长度较小者二分查找中位数,所以时间复杂度为O(log(min(m,n)))
法二:
两个数组的中位数是整个数组序列的第(m+n+1)/2小的和第(m+n+2)/2小的和的一半(m+n为奇数时也适用,
此时两个数相等)
所以就可以转化为求序列的第K小的数问题,假设第k小的数在nums1中是第i个位置，则合并之后
应有 nums2[k-i-2] <= nums1[i] <= nums2[k-i-1](保持nums1[i]左边比它小的数有k-1个)
所以可以在nums1中每次枚举第i= min(m,k/2)个数，寻找对应nums2中的第j = min(n,k-i)个数,
比较两个数的大小：
1.nums1[i] == nums2[j]:
说明此时刚好是第k小的数,直接返回
2.nums1[i] < nums2[j]:
说明此时nums[0..i-1]都不可能为寻找的目标，因为即便是其中最大的nums1[i]也最多是第k-1个数,
所以可将其前半部分去掉,而观察nums2[j:]这后半部分,也不可能是。所以最终在nums1[i:],nums2[:j]中寻找第k-i个元素
3.nums1[i] > nums2[j]:
同理将nums2的前半部分去掉,在nums1[:i],nums2[j:]中寻找第k-j的数

(注意此处有一个小细节是我采取的是每次将k值减半来寻找i,所以取的是下界，有可能会出现越界的情况,所以我采取的方法是
保证nums1的长度小于nums2,)
由于每次k减半，所以时间复杂度为O(log(m+n))


"""

###解法1
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        m,n = len(nums1),len(nums2)
        l,r, = 0,m
        while l <= r:
            i = (l+r)>>1
            j = (m+n+1)/2 - i
            if i > 0 and nums1[i-1] > nums2[j]: #不用判断j < n:i > 0 and m<=n --> j = (m+n+1)/2 - i < (m+n+1)/2 <= (2*n+1)/2 <= n --> j < n
                r = i - 1
            elif i < m and nums2[j-1] > nums1[i]:#同理:i < m and m<=n --> j = (m+n+1)/2 - i > (m+n+1)/2 - m = (n-m+1)/2 >= 0 --> j > 0 
                l = i + 1
            else:
                if i == 0:
                    maxleft = nums2[j-1]
                elif j == 0:
                    maxleft = nums1[i-1]
                else:
                    maxleft = max(nums1[i-1],nums2[j-1])

                #奇数情况
                if (m+n) & 1:
                    return maxleft
                if i == m:
                    minright = nums2[j]
                elif j == n:
                    minright = nums1[i]
                else:
                    minright = min(nums1[i],nums2[j])

                #偶数情况
                return (maxleft + minright) / 2.0


###解法2
class Solution(object):
    def getKth(self,nums1,m,nums2,n,k):
        if m > n:
            return self.getKth(nums2,n,nums1,m,k)
        if not nums1:
            return nums2[k-1]
        elif not nums2:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0],nums2[0])
        i = min(m,k/2)
        j = min(n,k-i)
        if nums1[i-1] == nums2[j-1]:
            return nums1[i-1]
        elif nums1[i-1] < nums2[j-1]:
            return self.getKth(nums1[i:],m-i,nums2[:j],j,k-i)
        else:
            return self.getKth(nums1[:i],i,nums2[j:],n-j,k-j)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1),len(nums2)
        lmedian,rmedian = (m+n+1)/2,(m+n+2)/2
        return (self.getKth(nums1,m,nums2,n,lmedian) + self.getKth(nums1,m,nums2,n,rmedian))/2.0
            