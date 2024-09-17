#
# @lc app=leetcode id=884 lang=python3
# @lcpr version=
#
# [884] Uncommon Words from Two Sentences
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        count = Counter(words)
        return [word for word in count if count[word] == 1]
# @lc code=end



#
# @lcpr case=start
# "this apple is sweet"\n"this apple is sour"\n
# @lcpr case=end

# @lcpr case=start
# "apple apple"\n"banana"\n
# @lcpr case=end

#

