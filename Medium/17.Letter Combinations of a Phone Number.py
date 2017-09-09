"""
思路:
很简单的用一个字典存储每个数字位对应的字符,一个个数字拓展即可
0和1的情况经过试验之后分别对应的是'*',' '.

"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dtos = {'0':' ','1':'*','2':'abc','3':'def','4':'ghi',
               '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        res = ['']
        for d in digits:
            res1 = []
            for ele in res:
                for ch in dtos[d]:
                    res1.append(ele+ch)
            res = res1
        return res
                