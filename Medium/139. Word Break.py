"""
最开始直接在wordDict中搜索解TLE了,应该是用dp来做,dp[i]表示s[0:i]是否能通过wordDict中的元素构成
有两种方法dp,一种是通过dp[j] (0<=j<i)来构造,若dp[j] == True and s[j:i] in wordDict 则dp[i]= true
第二种方法是先将wordDict中的每一个单词的首字母与其对应的单词添加到一个字典中,每当遇到一个dp[i]为true的值
在lettDict[s[i]]中查找word,若s[i+len(word)] == word,更新对应的dp[i+len(word)] = True
第二种方法以一定的空间损失换取了时间上的优化
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
        

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        from collections import defaultdict
        lettDict = defaultdict(list)
        for word in wordDict:
            lettDict[word[0]].append(word)
        for i in range(len(s)):
            if dp[i] == False or s[i] not in lettDict:
                continue
            if dp[-1] == True:
                return True
            for word in lettDict[s[i]]:
                length = len(word)
                if s[i:i+length] == word:
                    dp[i+length] = True
        return dp[-1]