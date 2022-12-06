import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(int(each) for each in re.findall(r"([0-9]+)",word)))