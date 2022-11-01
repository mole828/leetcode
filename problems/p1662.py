import itertools
from typing import List

def iter(words: List[str]):
    for s in words:
        for c in s:
            yield c

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a, b = iter(word1), iter(word2)
        for (c1,c2) in itertools.zip_longest(a,b):
            if c1 != c2:return False
        return True
