'''
题意：求单词列表words中为字符串S的子序列的单词个数. len(S) -> 5*10^4 len(words)->5*10^3
朴素的每个单词比较会超时
法一：
用一个字典按照从小到大的顺序存储每个在S中出现的字符的每个出现的下标位置, words中的单词最多为50 就可以用o(1)的时间判断每个单词
具体做法为用一个tag标记上一次匹配的字符的位置 每遍历完一个单词 找到一个子序列 结果+1

法二:
模拟trie树的结构，存储words中每个单词的首字母的一个字典，字典的value是(pos, word)元组，然后遍S中每个字符 每个字符都会得到与之匹配的字典中的word
每个单词匹配之后再把当前的下标及单词的元组存回字典， 每个单词的下标大于等于其长度时 说明得到一个匹配。
'''
法一：
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ch_idx = collections.defaultdict(list)
        for i, ch in enumerate(S):
            ch_idx[ch].append(i)
        ret = 0
        for word in words:
            nxt_idx = -1
            find = True
            for ch in word:
                if ch not in ch_idx:
                    find = False
                    break
                for idx in ch_idx[ch]:
                    if idx > nxt_idx:
                        nxt_idx = idx
                        break
                else:
                    find = False
                    break
            if find:
                ret += 1
        return ret

法二：

class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        tree = collections.defaultdict(list)
        for word in words:
            tree[word[0]].append((0,word))
        match = 0
        for ch in S:
            pos_words_list = tree[ch]
            tree[ch] = []
            
            for (i, word) in pos_words_list:
                if i + 1 >= len(word):
                    match += 1
                    continue
                tree[word[i+1]].append((i+1, word))
        return match

