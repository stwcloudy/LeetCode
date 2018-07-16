'''
将句子中在词典中有词根的词换成最短长度的词根
trie树
'''
class TrieNode():
    def __init__(self):
        self.count = 0
        self.next = {}
class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        self.root = TrieNode()
        def build_Trie():
            for word in dict:
                r = self.root
                for ch in word:
                    if ch not in r.next:
                        r.next[ch] = TrieNode()
                    r = r.next[ch]
                r.count += 1
        def replace_with_prefix(w):
            ret = ''
            find = True
            r = self.root
            for ch in w:
                if ch not in r.next:
                    return w
                else:
                    ret += ch
                    r = r.next[ch]
                    if r.count > 0:
                        return ret
            return w
        build_Trie()
        words = sentence.strip().split(' ')
        for i, w in enumerate(words):
            ret = replace_with_prefix(w)
            #print (ret)
            words[i] = ret
        return ' '.join(words)