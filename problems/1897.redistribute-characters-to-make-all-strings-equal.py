#
# @lc app=leetcode id=1897 lang=python3
#
# [1897] Redistribute Characters to Make All Strings Equal
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        counter = Counter()
        for word in words: counter.update(word)
        for key in counter:
            if counter[key]%length:
                return False
        return True
# @lc code=end

print(Solution().makeEqual(['aabc','bcdd']))