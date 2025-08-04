#
# @lc app=leetcode id=904 lang=python3
# @lcpr version=30204
#
# [904] Fruit Into Baskets
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        left = 0
        max_window = 0
        for fruit in fruits:
            window[fruit] += 1
            while len(window.keys()) > 2:
                k = fruits[left]
                window[k] -= 1
                if window[k] == 0:
                    del window[k]
                left += 1
            max_window = max(max_window, sum(window.values()))
        return max_window

        
# @lc code=end

# print(Solution().totalFruit([1,2,1]))
print(Solution().totalFruit([0,1,2,2]))

#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,2,2]\n
# @lcpr case=end

#

