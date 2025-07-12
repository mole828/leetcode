#
# @lc app=leetcode id=1900 lang=python3
# @lcpr version=30204
#
# [1900] The Earliest and Latest Rounds Where Players Compete
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache 
        def dfs(n: int, first: int, second: int) -> tuple[int, int]:
            if first + second == n + 1:
                return 1, 1

            if first + second > n + 1:
                first, second = n + 1 - second, n + 1 - first

            next_n = (n + 1) // 2 
            min_mid = 0 if second <= next_n else second - n // 2 - 1
            max_mid = second - first if second <= next_n else next_n - first
            earliest, latest = float('inf'), 0

            for left in range(first): 
                next_first = left + 1
                for mid in range(min_mid, max_mid): 
                    e, l = dfs(next_n, next_first, next_first + mid + 1)
                    earliest = min(earliest, e)
                    latest = max(latest, l)

            return earliest + 1, latest + 1

        return list(dfs(n, firstPlayer, secondPlayer))
        
# @lc code=end

print(Solution().earliestAndLatest(n=11, firstPlayer=2, secondPlayer=4))
print(Solution().earliestAndLatest(n=3, firstPlayer=2, secondPlayer=3))

#
# @lcpr case=start
# 11\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# 5\n1\n5\n
# @lcpr case=end

#

