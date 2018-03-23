"""
思路:
本题就是一个bfs的图问题,两个字符串距离为1(只有一个字符不同)即为有路径,要找最短路径
用bfs即可,但是用得不好,会TLE,采用了一个优化,普通的bfs是一个点扩展,层层探索,此处可以采用两个点(最初为起点和终点)
同时进行扩展,这样快一点(看见一个形象的比喻,池塘中从起点开始波纹扩散比起点终点同时扩散相遇慢)
始终选择结点集合少的扩展
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordDict = set(wordList)
        beginSet = set([beginWord])
        endSet = set([endWord])
        wordDict.discard(beginWord)
        step = 2
        while beginSet:
            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        nextSet.add(word[:i]+ch+word[i+1:])
            beginSet = wordDict & nextSet
            if beginSet & endSet:
                return step
            if len(beginSet) > len(endSet):
                beginSet,endSet = endSet,beginSet
            wordDict -= beginSet
            step += 1
        return 0
        