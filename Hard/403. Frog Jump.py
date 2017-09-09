"""
解法1:
先进行部分数据的加速判断,再回溯求解
代码中有:if i > 3 and stones[i] > 2*stones[i-1],此处大于3是因为如果存在的话前两个位置的pos固定为0,1.
若2,3都存在 从1最远能到达3,而3的下标最多为3,此后的pos 最远步骤从1直接到pos(求上界),则从pos到下一步最远的
位置为2*(pos-1) + 1,所以当下一个位置大于前面位置的两倍的时候直接返回False

解法2：
用一个字典存储上一步到达pos位置处所走的units数
step[1] = 1
表示到达1这个位置所走的步数只有1(0->1)
step[i] = (2,3)
表示从i-2,i-3处分别走两步三步到达i位置

"""

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        if stones[1] != 1:
            return False
        ###此处优化少了会TLE
        for i in range(n):
            if i > 3 and stones[i] > 2*stones[i-1]:
                return False
        def dfs(stones,pos,step):
            if pos + step - 1 == stones[-1] or pos + step == stones[-1] or pos + step + 1 == stones[-1]:
                return True
            if pos + step + 1 in stones:
                if dfs(stones,pos+step+1,step+1):
                    return True
            if pos + step in stones:
                if dfs(stones,pos+step,step):
                    return True
            if step > 1 and pos + step - 1 in stones:
                if dfs(stones,pos+step-1,step-1):
                    return True
            return False
        return dfs(stones,0,1)

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        if stones[1] != 1:
            return False
        ##step字典存储的是上一次到达pos位置的跳的units
        step = {pos:set() for pos in stones}
        step[1].add(1)
        for i in range(1,n):
            pos = stones[i]
            for move in step[pos]:
                for next_move in range(move-1,move+2):
                    if next_move > 0 and pos+next_move in step:
                        step[pos+next_move].add(next_move)
        if len(step[stones[-1]]) >= 1:
            return True
        return False