from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            isConsistentString = True
            for char in word:
                if char not in allowed:
                    isConsistentString = False
            if isConsistentString:
                ans += 1
        return ans