"""
这题与Jump Game 不同,本题默认所给数据一定能够到达终点,求最小步数
思路:
preReach,maxReach分别记录上一个能到达的最远距离和当前能到达的最远距离,
每次到达一个点之后将i+nums[i]与最远距离相比较 若大则更新maxReach
如果当前位置的下标大于preReach,说明需要将step+1以到达当前位置
遍历一遍数组即可O(N)
其实本质是bfs扩展
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step,preReach,maxReach = 0,0,0
        for i in range(len(nums)):
            if i > preReach:
                step += 1
                preReach = maxReach
            maxReach = max(maxReach,i + nums[i])
        return step