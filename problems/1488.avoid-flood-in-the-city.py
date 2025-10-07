#
# @lc app=leetcode id=1488 lang=python3
# @lcpr version=30204
#
# [1488] Avoid Flood in The City
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full_day = {}  # lake -> 装满日
        dry_day = SortedList()  # 未被使用的抽水日
        for i, lake in enumerate(rains):
            if lake == 0:
                ans[i] = 1  # 先随便选一个湖抽干
                dry_day.add(i)  # 保存抽水日
                continue
            if lake in full_day:
                j = full_day[lake]
                # 必须在 j 之后，i 之前把 lake 抽干
                # 选一个最早的未被使用的抽水日，如果选晚的，可能会导致其他湖没有可用的抽水日
                k = dry_day.bisect_right(j)
                if k == len(dry_day):
                    return []  # 无法阻止洪水
                d = dry_day[k]
                ans[d] = lake
                dry_day.discard(d)  # 移除已使用的抽水日
            full_day[lake] = i  # 插入或更新装满日
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,0,0,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,0,1,2]\n
# @lcpr case=end

#

