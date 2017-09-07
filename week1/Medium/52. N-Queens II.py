"""
这题只要求方案数,我们可以用位运算来提高速度m
https://zhuanlan.zhihu.com/p/22873368该链接讲解求解N皇后的几种方法
对于两条对角线的位置,与行列的关系是
45度角方向pie所在的编号为row+col(分别表示行列编号)
135度角方向的na所在编号为n-1-row+col
pie,na分别有2*n-1条
观察棋盘上的位置在51题中,我们每次都是遍历所有列所在的位置,但是其实随着递归加深
能使用的列越来越少,所以换种思路找能使用的列,
shu,pie,na的哪些二进制为1表示当前位置不可用,所以shu|pie|na表示所有不能使用的位置
~(shu|pie|na)的最右边n位则表示所有能使用的位置,为了保证只取最右n位,再&上一个bound=(1<<n)-1(1...111 -->n个1)
这样 当前行所在所有能用的位置为:available = bound & ~(shu|pie|na)
每次取最右的位置的1,递归进行下一行的搜索
注意的是pie在row行影响的是第j列,在row+1行则影响j-1列,所以需要左移一位((pie|na)<<1),na同理
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        bound = (1<<n) - 1
        def dfs(row,shu,pie,na):
            available = bound & ~(shu|pie|na)
            while available:
                p = available & -available
                available ^= p
                if row == n-1:
                    self.ans += 1
                dfs(row+1,shu|p,(pie|p)<<1,(na|p)>>1)
        dfs(0,0,0,0)
        return self.ans
            