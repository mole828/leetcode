class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = set()
        for c in s:
            if c in d:return c
            d.add(c)