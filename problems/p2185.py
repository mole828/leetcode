from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if pref in word and word.index(pref)==0:ans+=1
        return ans