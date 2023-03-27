'''
阅读理解
'''
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        sn, tn = len(s), len(t)
        ans = 0
        for i in range(sn):
            for j in range(tn):
                w = 0
                for k in range(min(sn - i, tn - j)):
                    if s[i + k] != t[j + k]:
                        w += 1
                    if w == 1:
                        ans += 1
                    elif w > 1:
                        break
        return ans