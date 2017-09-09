"""
思路:
简单的栈的应用
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                st.append(p)
            else:
                if p == ')':
                    if not st or st[-1] != '(':
                        return False
                    else:
                        st.pop()
                elif p == ']':
                    if not st or st[-1] != '[':
                        return False
                    else:
                        st.pop()
                elif p == '}':
                    if not st or st[-1] != '{':
                        return False
                    else:
                        st.pop()           
                #其他非括号字符
                else:
                    return False
        if not st:
            return True
        return False