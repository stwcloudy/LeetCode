'''
题意:
车子油箱无限容量，初始有个startFuel的油量,距离目标点的距离为target,途中有加油站,用stations表示
stations[0]表示距离起始点的距离,stations[1]表示可以加的油量，每次加油把当前加油站的油量全部加完，求最小停站加油次数能到达target
如果不能达到返回-1
思路:
动态规划dp[i] 表示i次停车能达到的最远距离
则更新dp[i]时 若dp[i-1] >= stations[j][0] 表示前i-1次加油至少能够到达j加油站
所以dp[i] = max(dp[i], dp[i-1] + stations[j][1])
加油次数从当前i->1次 逆序遍历。 因为当前次数要加1的话，如果顺序遍历，则每次更新k的时候 k-1实质上已经是在j加油站停过之后更新的数据了
所以逆序能够保证每个加油站只使用一次
'''
class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        n = len(stations)
        dp = [startFuel] + [0]*(n)
        res = n + 2
        if startFuel >= target:
            return 0
        for i in range(n):
            for j in range(i+1,0,-1):
                if dp[j-1] >= stations[i][0]:
                    dp[j] = max(dp[j], dp[j-1] + stations[i][1])
                    if dp[j] >= target:
                        res = min(res,j)
            #print (dp)
        if res == n + 2:
            return -1
        return res