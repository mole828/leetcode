#
# @lc app=leetcode id=3577 lang=python3
#
# [3577] Count the Number of Computer Unlocking Permutations
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        counter = Counter(complexity)
        start_complexity = complexity[0]
        min_complexity = min(counter.keys())
        if start_complexity != min_complexity:
            return 0
        if counter[min_complexity] > 1:
            return 0
        ans = 1
        for v in range(n-1, 0, -1):
            ans = ans * v % MOD
        return ans
        
# @lc code=end

print(Solution().countPermutations([1,2,3]))