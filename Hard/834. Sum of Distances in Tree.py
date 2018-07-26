'''
N个点,N-1条边构成一个无向图，返回ans列表ans[i]表示的是i到其他所有点的距离之和。
思路:
对于两个相邻的节点x,y来说, 以x,y边将整个图分为两个部分, 则有：
ans[x] = sub[x] + sub[y] + count[y]   1
ans[y] = sub[y] + sub[x] + count[x]   2
以上两个等式中ans[i]表示所求结果, sub[i]则是以i为根的子树的(减掉边x,y之后的子树)距离和,count[i]表示的是
以i为根的子树的节点个数(包括i), 根据上述表达,ans[x] - ans[y] = count[y] - count[x]    3
因为该无向图可以以任意节点为根构成一棵树,所以
1. 先第一遍后根dfs遍历,算出每个节点的count[i]和sub[i],则根节点的ans[root]==sub[root];
2. 第二遍先根遍历,根据3式,可以得出ans[child] = ans[fa] + (N - count[child]) - count[child] = ans[fa] + N - 2*count[child]
就可以算出每个节点的ans值
'''
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        g = collections.defaultdict(set)
        count = [1]*N
        res = [0]*N
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        def dfs(root=0,fa=None):
            for v in g[root]:
                if v != fa:
                    dfs(v,root)
                    count[root] += count[v]
                    res[root] += res[v] + count[v]
        def get_ans(root=0,fa = None):
            for v in g[root]:
                if v != fa:
                    res[v] = res[root] + N - 2*count[v]
                    get_ans(v,root)
        dfs()
        get_ans()
        return res
        