#
# @lc app=leetcode id=3186 lang=python3
#
# [3186] Maximum Total Damage With Spell Casting
#

# @lc code=start
from functools import cache
from typing import Counter, List


class Solution:
    # timeout
    def maximumTotalDamage(self, power: List[int]) -> int:
        kv = {}
        for p in power:
            if p not in kv:
                kv[p] = 0
            kv[p] += p
        keys = sorted(kv.keys())
        @cache
        def dp(i: int) -> int:
            key = keys[i]
            total = kv[key]
            # pick this key
            picks = max((dp(next_index) for next_index in range(i+1, len(keys)) if keys[next_index] > key+2), default=0)
            pick = total + picks
            # not pick this key
            not_pick = max([
                picks,
                dp(i+1) if i+1 < len(keys) and keys[i+1] <= key+2 else 0,
                dp(i+2) if i+2 < len(keys) and keys[i+2] <= key+2 else 0,
            ])
            return max(pick, not_pick)
        
        return dp(0)
    
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt)

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = a[i]
            j = i
            while j and a[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])

        return dfs(len(a) - 1)

        
# @lc code=end

print(Solution().maximumTotalDamage([7,1,6,6]))