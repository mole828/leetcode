from collections import Counter


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counter = Counter('croak')
        for k in counter: counter[k] -= 1
        m = 0
        for c in croakOfFrogs:
            counter[c]+=1
            i = 'croak'.index(c)
            if i!=0:
                a, b = [counter['croak'[j]] for j in [i-1, i]]
                if b > a:return -1
            m = max(m,*counter.values())
            if 0 not in set(counter.values()) :
                for k in counter: counter[k] -= 1
        return m if set(counter.values()) == set([0]) else -1