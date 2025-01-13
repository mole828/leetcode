#
# @lc app=leetcode id=3223 lang=python3
# @lcpr version=
#
# [3223] Minimum Length of String After Operations
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        char_frequency_map = Counter(s)

        delete_count = 0
        for frequency in char_frequency_map.values():
            if frequency % 2 == 1:
                delete_count += frequency - 1
            else:
                delete_count += frequency - 2
        return len(s) - delete_count
# @lc code=end



#
# @lcpr case=start
# "abaacbcbb"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n
# @lcpr case=end

#

