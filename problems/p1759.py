class Solution:
    def countHomogenous(self, s: str) -> int:
        i,j = 0,0
        suu = 0
        t = 1
        l = len(s)
        while i < l and j < l:
            if s[i] == s[j]:
                suu = suu + t
                j = j + 1
                t = t + 1
            else:
                t = 1
                i = j
        return suu % (10**9 + 7)