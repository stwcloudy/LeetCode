"""
一开始没有转换思维，还是顺着想从左上->右下dp,后来发现
从右下开始->左上dp更简单，hp[i][j]表示到达pos(i,j)时的最小血量，
从右下开始的话，按照left,up的规则，更新hp[i][j],使其尽量小，注意边界情况即可。
"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m,n = len(dungeon),len(dungeon[0])
        hp = [[0]*n for _ in range(m)]
        print m,n
        print 'start'
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m - 1 and j == n - 1:
                    hp[i][j] = max(1,1 - dungeon[i][j])
                elif i == m - 1:
                    hp[i][j] = max(1, hp[i][j+1] - dungeon[i][j])
                elif j == n - 1:
                    hp[i][j] = max(1,hp[i+1][j] - dungeon[i][j])
                else:
                    hp[i][j] = max(1,min(hp[i+1][j],hp[i][j+1]) - dungeon[i][j])
        return hp[0][0]