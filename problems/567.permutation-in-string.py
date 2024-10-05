#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=
#
# [567] Permutation in String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        def window():
            for i in range(len(s1), len(s2)):
                yield s2[i - len(s1)], s2[i]

        for a, b in window():
            if c1 == c2:
                return True
            c2[b] += 1
            c2[a] -= 1

        return c1 == c2
        
# @lc code=end



#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

