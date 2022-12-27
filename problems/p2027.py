class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                i = i + 3
                res += 1
            else:
                i = i + 1
        return res