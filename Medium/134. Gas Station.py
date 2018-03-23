"""
思路一:
思路一基于这样的两个事实,
1.positionA首次不能到达的位置为positionB,则A-B间的任意一个位置都不能到达B
2.如果全部的gas的和加起来大于cost的和则一定有一个解
证明:
假设total = sigma(gas[i]-cost[i])>=0,则假设有某个i处,使得(gas[0]-cost[0]+...+gas[i]-cost[i])
最小,有:
gas[i+1]-cost[i+1]>=0
gas[i+1]-cost[i+1] + gas[i+2]-cost[i+2]>=0
gas[i+1]-cost[i+1]+...+gas[n-1]-cost[i-1]>=0
而对于任意的j<i：
gas[0]-cost[0]+...+gas[j]-cost[j]+gas[i+1]-cost[i+1]+...+gas[n-1]-cost[n-1]>=
gas[0]-cost[0]+...+gas[i]-cost[i+1]+gas[i+1]-cost[i+1]+...+gas[n-1]-cost[n-1]>=0
所以,i+1的位置处就是开始的地方
思路二:
用双指针的思路,start,end指针初始分别指向末尾和开始处,当前剩余gas大于等于0时,移动end指针.
反之移动start指针,过程始终保持start>end
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start,total,left = 0,0,0
        for i in range(len(gas)):
            left = gas[i] + left - cost[i]
            if left < 0:
                start = i + 1
                total += left
                left = 0
        return -1 if total + left < 0 else start

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start,end = len(gas)-1,0
        diff = gas[start] - cost[start]
        while start > end:
            if diff >= 0:
                diff += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                diff += gas[start] - cost[start]
        return start if diff >= 0 else -1