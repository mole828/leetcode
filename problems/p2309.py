class Solution:
    def greatestLetter(self, s: str) -> str:
        upper = set([c for c in s if c==c.upper()])
        summary = set(s)
        ans = list(set(c for c in upper if c.lower() in summary))
        if len(ans):return sorted(ans)[-1]
        return ''