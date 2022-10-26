from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        for x, y in zip_longest(word1, word2):
            if x: ans+=x
            if y: ans+=y
        return ans