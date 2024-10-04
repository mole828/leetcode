#
# @lc app=leetcode id=2491 lang=python3
# @lcpr version=
#
# [2491] Divide Players Into Teams of Equal Skill
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[-1]
        result = 0
        for i in range(n // 2):
            a, b = skill[i], skill[n - 1 - i]
            if a + b!= target:
                return -1
            result += a * b
        return result
        
# @lc code=end



#
# @lcpr case=start
# [3,2,5,1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3]\n
# @lcpr case=end

#

