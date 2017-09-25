"""
承接139题,前题只需要判断是否能够组合成s,本题需要找出路径,我的思路是把中间过程记录下来,
因为到达某个位置i的组合情况可能不止一种,所以我用一个dict来保存路径,pre[i]表示的是从之前的哪个位置到达i
最后再dfs搜索路径(个人感觉自己的这个想法虽然AC但是太过于冗杂)
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        from collections import defaultdict
        lettDict = defaultdict(list)
        pre,res = defaultdict(list),[]
        pre[0] = [-1]
        for word in wordDict:
            lettDict[word[0]].append(word)
        def printpath(res,path,pre,idx):
            if idx == -1:
                res.append(' '.join(path[::-1]))
            for i in pre[idx]:
                tmp = path + [s[i:idx]] if i != -1 else path
                printpath(res,tmp,pre,i)
        for i in range(len(s)):
            if dp[i] == False or s[i] not in lettDict:
                continue
            for word in lettDict[s[i]]:
                length = len(word)
                if s[i:i+length] == word:
                    dp[i+length] = True
                    pre[i+length].append(i)
        print pre
        if dp[-1]:
            printpath(res,[],pre,len(s))
        return res