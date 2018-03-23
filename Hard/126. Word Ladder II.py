
"""
思路
和127题的过程一样,只是在过程中多了一个记录每个单词的前一步的单词的路径,这样
要得到最后的全部路径,则进行dfs遍历即可

"""
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        def getPath(pre,endWord,path,res):
            if not pre[endWord]:
                path += [endWord]
                res.append(path[::-1])
            for ele in pre[endWord]:
                getPath(pre,ele,path+[endWord],res)
        from collections import defaultdict
        pre = defaultdict(list)
        wordDict = set(wordList)
        beginSet = set([beginWord])
        endSet = set([endWord])
        wordDict.discard(beginWord)
        res = []
        while beginSet:
            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        nextWord = word[:i]+ch+word[i+1:]
                        if nextWord in wordDict:
                            nextSet.add(nextWord)
                            pre[nextWord].append(word)
            beginSet = wordDict & nextSet
            if beginSet & endSet:
                getPath(pre,endWord,[],res)
                return res
            # if len(beginSet) > len(endSet):
            #     beginSet,endSet = endSet,beginSet
            wordDict -= beginSet
        return res