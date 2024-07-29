#
# @lc app=leetcode id=1395 lang=python3
# @lcpr version=
#
# [1395] Count Number of Teams
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# Time Limit Exceeded, 63/72 cases passed (N/A)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)
        for i in range(n):
            vi = rating[i]
            for j in range(i+1, n):
                vj = rating[j]
                for k in range(j+1, n):
                    vk = rating[k]
                    if vi>vj>vk or vi<vj<vk:
                        count += 1
        return count
    
from sortedcontainers import SortedList
import bisect

# TODO 
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sl1 = SortedList()
        sl2 = SortedList(rating)
        res = 0
        for j in range(len(rating)):
            sl2.remove(rating[j])
            sl1Index = bisect.bisect(sl1, rating[j])
            sl2Index = bisect.bisect(sl2, rating[j])
            res += sl1Index * (len(sl2) - sl2Index)
            res += (len(sl1) - sl1Index) * sl2Index
            sl1.add(rating[j])
        return res

# @lc code=end



#
# @lcpr case=start
# [2,5,3,4,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#

