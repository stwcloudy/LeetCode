'''
给定一组非负数,两个人轮流删数,当某人不管擦除任何数都导致异或的结果为0,则他输
Alice先手
1）如果xor == 0，那就说明Alice已经赢了，因为上一把Bob的行为已经导致了xor == 0。

2）如果xor != 0，并且数组的长度为偶数，那么Alice一定会赢。这是因为：当数组长度为偶数的时候，不可能所有的数都相同（否则xor == 0）。此时Alice总是可以找到两个不同的数，并且erase掉其中一个，
这样一定不会引起xor == 0。所以Alice一定会赢。
再看看如果xor != 0 && nums.size() % 2 != 0的时候，会发生什么吧：Alice此时会被迫擦掉一个数，如果擦掉的这个数引起了xor == 0，那么她就立刻输了；否则她擦掉的数虽然不会导致xor == 0，
但是此时数组中剩下了偶数个元素，那么Bob就可以采用和Alice相同的策略把Alice干掉，因为此时xo ！= 0 && nums.size() == 0，满足上面分析中的条件2）。
所以Alice会赢当且仅当xor == 0 || nums.size() % 2 == 0。
'''
class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        for num in nums:
            s ^= num
        return True if (s == 0 or not len(nums)%2) else False