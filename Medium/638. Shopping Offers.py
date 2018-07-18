'''
每种物品有一个价格,商店提供几种特价的打包优惠，给定所需要物品的数量，求如何利用这些特价礼包可以使购买价格最低.
使用特价礼包时, 每种物品的数量都不得超过需要的数量,即便它的价格可能更低。
prices=[2,3,4], special=[[1,1,0,4],[2,2,1,9]], needs=[1,2,1]
Output: 11
如上第一个为prices数组 表示每种物品的价格，第二个列表中每个是一种特惠,最后一个元素为该特惠的价格，前面表示提供的每种物品的数量, [2,2,1,9]虽然更低,但是第一种
物品买了两个 超过所需.
思路: 
如果使用了某个特惠之后,花了x的钱,需要购买的物品还剩remain,则所剩下的问题变成子问题
prices不变, special不变 needs = remain
所以可以直接用递归来解决该问题,但是由于普通递归会遇到很多重复子问题,所以采用dfs+memorization。dp[str(needs) or tuple(needs)] = x 表示需求为needs时,
所需要花的钱
'''

class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        valid_offers = []
        for s in special:
            if all(a <= b for a,b in zip(s[:-1],needs)):
                valid_offers.append(s)
        dp = collections.defaultdict(int)
        #print (valid_offers)
        def dfs(offers, needs):
            if str(needs) in dp:
                return dp[str(needs)]
            for i, count in enumerate(needs):
                dp[str(needs)] += price[i]*count
            for sp in offers:
                amount, cost = sp[:-1],sp[-1]
                remain = []
                for a,b in zip(amount, needs):
                    remain.append(b-a)
                if any(x < 0 for x in remain):
                    continue
                dp[str(needs)] = min(dp[str(needs)],cost + dfs(offers, remain))
            return dp[str(needs)]
        dfs(valid_offers, needs)
        return dp[str(needs)]