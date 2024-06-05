#
# @lc app=leetcode id=1002 lang=python3
# @lcpr version=
#
# [1002] Find Common Characters
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wc = [Counter(word) for word in words]
        count = reduce(lambda a, b: a & b, wc)
        return count.elements()
# @lc code=end



#
# @lcpr case=start
# ["bella","label","roller"]\n
# @lcpr case=end

# @lcpr case=start
# ["cool","lock","cook"]\n
# @lcpr case=end

#

