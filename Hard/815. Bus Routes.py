'''
给个routes线路,每个线路记录公车经过的站点,再给定一个S,T站点，从S到T坐的最少的公交车数是多少

解法:
bfs
将每个站点经过的公车记录下来,从S开始，bfs遍历每条路线上的站点,直至找到T
'''
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        st_routes = collections.defaultdict(set)
        for i,route in enumerate(routes):
            for st in route:
                st_routes[st].add(i)
        q = [S]
        lines = 1
        visited = set()
        while q:
            n = len(q)
            for _ in range(n):
                st = q.pop(0)
                for route in st_routes[st]:
                    if route not in visited:
                        visited.add(route)
                        for sta in routes[route]:
                            if sta == T:
                                return lines
                            q.append(sta)
            lines += 1
        return -1
                  