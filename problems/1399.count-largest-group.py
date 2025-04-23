#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
from collections import Counter
from typing import Optional


class Solution:
    def countLargestGroup(self, n: int) -> int:
        c = Counter()
        for i in range(1, n+1):
            s = [int(c) for c in str(i)]
            sum_s = sum(s)
            c[sum_s] += 1
        print(c)
        count = 0
        last_value: Optional[int] = None
        for key, value in c.most_common():
            if not last_value:
                last_value = value
                count += 1
                continue
            if value == last_value:
                count += 1
            else:
                break
        return count

            
# @lc code=end

print(Solution().countLargestGroup(n=13))