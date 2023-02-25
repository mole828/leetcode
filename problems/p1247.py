class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        ns1 = ""
        ns2 = ""
        for ss1, ss2 in zip(s1, s2):
            if ss1 != ss2:
                ns1 += ss1
                ns2 += ss2
        res = 0
        idx = 0
        while len(ns1) > 1 and idx < len(ns1)-1:
            if ns1[idx] == ns1[idx+1]:
                res += 1
                ns1 = ns1[:idx] + ns1[idx+2:]
                ns2 = ns2[:idx] + ns2[idx+2:]
                if idx > 1:
                    idx -= 2
                else:
                    idx = -1
            idx += 1
        if len(ns1) % 2 != 0: 
            return -1
        return res + len(ns1) // 4 * 2 + len(ns1) % 4