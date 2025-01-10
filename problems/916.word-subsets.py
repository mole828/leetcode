#
# @lc app=leetcode id=916 lang=python3
# @lcpr version=
#
# [916] Word Subsets
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import Counter, List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wc1List = [(s,Counter(s)) for s in words1]
        wc2List = [Counter(s) for s in words2]
        wc2 = Counter()
        for wc in wc2List:
            wc2 |= wc
        res = []
        for s,wc1 in wc1List:
            sub = wc2 - wc1
            if not sub:
                res.append(s)
        return res

        
# @lc code=end



#
# @lcpr case=start
# ["amazon","apple","facebook","google","leetcode"]\n["e","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["amazon","apple","facebook","google","leetcode"]\n["l","e"]\n
# @lcpr case=end

#

