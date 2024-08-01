#
# @lc app=leetcode id=2678 lang=python3
# @lcpr version=
#
# [2678] Number of Senior Citizens
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(line[-4:-2])>60 for line in details)
# @lc code=end



#
# @lcpr case=start
# ["7868190130M7522","5303914400F9211","9273338290F4010"]\n
# @lcpr case=end

# @lcpr case=start
# ["1313579440F2036","2921522980M5644"]\n
# @lcpr case=end

#

