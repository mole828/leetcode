from collections import Counter, defaultdict

# 用例太差了, 不推荐

class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        res = {}
        base = len(s) // 4
        temp = 0
        for i,v in enumerate(count.keys()):
            if count[v] > base:
                res[v] = count[v] - base
                temp += res[v]
        if temp ==0:
            return temp
        print(res)
        window = defaultdict(int)
        l,r = 0,0
        ans = len(s)
        while r <= len(s):
            r += 1
            while all(s[l:r].count(i) >= res[i] for i in res.keys()):
                ans = min(ans, r-l)
                l+=1
        return ans