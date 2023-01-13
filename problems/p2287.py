from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count=dict(Counter(s))
        t_count=dict(Counter(target))
        copies=100
        for key in t_count.keys():
            copies=min(s_count.get(key,0)//t_count[key],copies)
        return copies