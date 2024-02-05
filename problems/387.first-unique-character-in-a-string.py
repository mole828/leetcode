#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for index,char in enumerate(s):
            if count[char] == 1:
                return index
        return -1
    
# @lc code=end

