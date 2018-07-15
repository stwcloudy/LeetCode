'''
题意 字符串中出现唯一字符的个数称为unique(s),给定一个字符串S求出其所有子字符串的唯一字符的个数和
如果要遍历所有的子串 则一共要遍历O(n^2)的数量; 超时。
换个思路， 思考每个字符对于结果的贡献, 对于字符串s='xxxAxxxAxxxxA'中的A字符来说,如果要使第二个A在子串中是unique的,
则所取位置要在第一个A和第三个A之间的字符,即'xxxAxxxx' 其个数为(second-first)*(third-second) 其中first，second，third是A所在位置下标
这样就将处理子串问题转化为原始串中每个字符作为unique字符时的个数的总和问题。 时间复杂度为O(n), 为了处理两个边界,每个字符的下标第一个为-1 最后一个
为字符长度

'''
class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        n = len(S)
        res = 0
        for i,ch in enumerate(S):
            prev, cur = index[ch]
            res += (cur - prev) * (i - cur)
            index[ch] = [cur, i]
        for ch in index:
            prev, cur = index[ch]
            res += (cur - prev) * (n - cur)
        return res % (10**9 + 7)
            
        
class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        ch_idx = collections.defaultdict(list)
        for i, ch in enumerate(S):
            ch_idx[ch].append(i)
        for ch in ch_idx:
            ch_idx[ch].insert(0,-1)
            ch_idx[ch].append(n)
        res = 0
        for _, idx_list in ch_idx.items():
            #print (idx_list)
            for i in range(1,len(idx_list)-1):
                res += (idx_list[i] - idx_list[i-1]) * (idx_list[i+1] - idx_list[i])
        return res%(10**9 + 7)