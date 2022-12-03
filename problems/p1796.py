class Solution:
    def secondHighest(self, s: str) -> int:
        return sorted([-1,-1]+list(set([int(c) for c in s if c.isdigit()])))[-2]
    