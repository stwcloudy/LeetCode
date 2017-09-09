"""
思路:
使用一个滑动窗口维护当前在words中出现的单词(连续出现
1.先用一个字典d将words中单词出现的次数统计出来;
2.由于每个单词的长度都一样,所以我们在外层循环中开始位置只需要遍历(0,word_len)中选取首字母开始遍历
3.用另一个win的字典维护当前窗口中的word的次数,每当某个word次数>d[word]使,需要收缩左窗口边界直到合法
4.start,end分别表示窗口的前后端,若当前word不是在words中出现,start直接跳到当前end所在位置,
并且将win置空
5.当窗口内的word刚好和d中的匹配时,将此时的start下标加入结果
"""

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        word_len = len(words[0])
        res = []
        for i in range(word_len):
            start,end = i,i
            win = {}
            while end + word_len <= len(s):
                word = s[end:end+word_len]
                end += word_len
                if word not in words:
                    start = end
                    win = {}
                else:
                    if word not in win:
                        win[word] = 1
                    else:
                        win[word] += 1
                    while win[word] > d[word]:
                        win[s[start:start+word_len]] -= 1
                        start += word_len
                    if end - start == word_len*len(words):
                        res.append(start)
        return res