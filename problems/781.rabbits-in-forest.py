#
# @lc app=leetcode id=781 lang=python3
# @lcpr version=30204
#
# [781] Rabbits in Forest
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
import math
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count: dict[int,int] = defaultdict(int)
        for a in answers:
            count[a] += 1
        ans = 0
        for k, v in count.items():
            group_max = k + 1
            group = math.ceil( v / group_max )
            ans += group * group_max
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [10,10,10]\n
# @lcpr case=end

#

