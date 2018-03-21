"""
题意：一个长度为n+1的数组，数组中的数字只在1-n之间，找出重复的数字
法1:
数字在1-n之间，所以将数组重排之后，在位置0处的即为重复数字，所以可以利用下标和数字之间的关系来做
从位置1处开始扫描数组，当扫描到下标i处数字为m，如果m == i则继续扫描，如果不是将其和第m个数比较
若相等，则返回该数字即为重复的，不相等则交换，将m放到它的位置，由于某个数最多交换两次回到原有位置，所以时间复杂度为O(n)

法2:
借鉴于floyd判圈法
对于一个存在环的链表（或其他数据结构），用两个指针，slow，fast，从起点开始，slow一次走一步，fast一次走两步，由于环的存在，则两者必定会相遇，
要判断环的起点。
假设起点到环的起点距离为m，已经确定有环，环的周长为n，（第一次）相遇点距离环的起点的距离是k。那么当两者相遇时，
慢指针移动的总距离为i，i = m + a * n + k，因为快指针移动速度为慢指针的两倍，那么快指针的移动距离为2i，2i = m + b * n + k。
其中，a和b分别为慢指针和快指针在第一次相遇时转过的圈数。我们让两者相减（快减慢），那么有i = (b - a) * n。即i是圈长度的倍数。
利用这个结论我们就可以理解Floyd解法为什么能确定环的起点。将一个指针移到链表起点，另一个指针不变，即距离链表起点为i处，两者同时移动，每次移动一步。
当第一个指针前进了m，即到达环起点时，另一个指针距离链表起点为i + m。考虑到i为圈长度的倍数，可以理解为指针从链表起点出发，走到环起点，然后绕环转了几圈，所以第二个指针也必然在环的起点。即两者相遇点就是环的起点
在该题中也一样
将数组下标和数值一一映射起来，如不存在重复的例子
0 1 2
2 3 1
0-->2-->1-->3。。结束 无环
而，
0 1 2 3 
2 1 3 1
0-->2-->3-->1-->1-->1...
存在环，而且环的起点就是重复数字
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp
        return nums[0]
                

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow