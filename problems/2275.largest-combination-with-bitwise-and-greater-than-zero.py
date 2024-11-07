#
# @lc app=leetcode id=2275 lang=python3
# @lcpr version=
#
# [2275] Largest Combination With Bitwise AND Greater Than Zero
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counter = Counter()
        for x in candidates:
            s = reversed(bin(x).removeprefix('0b'))
            for i, b in enumerate(s):
                if b == '1':
                    counter[i] += 1
        print(counter)
        return counter.most_common()[0][1]
   
# @lc code=end

print(Solution().largestCombination([16,17,71,62,12,24,14]))

#
# @lcpr case=start
# [16,17,71,62,12,24,14]\n
# @lcpr case=end

# @lcpr case=start
# [8,8]\n
# @lcpr case=end

#

