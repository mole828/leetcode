#
# @lc app=leetcode id=2147 lang=python3
#
# [2147] Number of Ways to Divide a Long Corridor
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from functools import reduce


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        list_count = [1 if corridor[0]=='S' else 0]
        for c in corridor[1:]:
            if c == 'S':
                list_count.append(list_count[-1]+1)
            else:
                list_count.append(list_count[-1])
        index = Counter(list_count)
        output = 1
        for key in index:
            if key==list_count[-1]:
                if key%2!=0 or key<2:
                    continue
                break
            if key==0:
                continue
            if key%2==0:
                output *= index[key]
        else:
            output = 0
        return output % (10**9+7)
# @lc code=end

print(Solution().numberOfWays(corridor = "SSPPSPS"))
