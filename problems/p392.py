class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        while ls and lt:
            a,b = ls.pop(),lt.pop()
            if a!=b:
                ls.append(a)
        return not ls
    