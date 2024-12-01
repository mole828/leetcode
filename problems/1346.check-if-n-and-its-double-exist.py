#
# @lc app=leetcode id=1346 lang=python3
# @lcpr version=30204
#
# [1346] Check If N and Its Double Exist
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or num % 2 == 0 and num // 2 in seen:
                return True
            seen.add(num)
        return False
# @lc code=end



#
# @lcpr case=start
# [10,2,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,7,11]\n
# @lcpr case=end

#

