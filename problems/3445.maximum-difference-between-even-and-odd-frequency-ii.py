#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
from collections import defaultdict
from math import inf
from typing import Optional


class Solution:
    # Time Limit Exceeded, 667/690 cases passed
    def maxDifference0(self, s: str, k: int) -> int:
        max_diff: Optional[int] = None
        for left in range(len(s) - k + 1):
            # print(left)
            for right in range(left + k, len(s)+1):
                # print(s[left:right])
                counter: dict[str, int] = defaultdict(int)
                for c in s[left:right]:
                    counter[c] += 1
                odd_values: list[int] = []
                even_values: list[int] = []
                for v in counter.values():
                    if v % 2 == 0:
                        even_values.append(v)
                    else:
                        odd_values.append(v)
                if even_values and odd_values:
                    max_odd = max(odd_values)
                    min_even = min(even_values)
                    max_diff = max( max_odd - min_even, max_diff if max_diff else -10**7 )
        return max_diff if max_diff else -1
    
    def maxDifference(self, _s: str, k: int) -> int:
        s: list[int] = list(map(int, _s))
        ans: float = -inf
        for x in range(5):
            for y in range(5):
                if y == x:
                    continue
                cur_s = [0] * 5
                pre_s = [0] * 5
                min_s = [[inf, inf], [inf, inf]]
                left = 0
                for i, v in enumerate(s):
                    cur_s[v] += 1
                    r = i + 1
                    while r - left >= k and cur_s[x] > pre_s[x] and cur_s[y] > pre_s[y]:
                        p, q = pre_s[x] & 1, pre_s[y] & 1
                        min_s[p][q] = min(min_s[p][q], pre_s[x] - pre_s[y])
                        pre_s[s[left]] += 1
                        left += 1
                    if r >= k:
                        ans = max(ans, cur_s[x] - cur_s[y] - min_s[cur_s[x] & 1 ^ 1][cur_s[y] & 1])
        return int(ans)

# @lc code=end

# print(Solution().maxDifference(s = "1122211", k = 3))
print(Solution().maxDifference(_s = "44114402", k = 7))