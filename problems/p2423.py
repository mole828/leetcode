from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for key in counter.keys():
            counter[key] -= 1
            if len(set(counter.values())-set([0]))==1:return True
            counter[key] += 1
        return False