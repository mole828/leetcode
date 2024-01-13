#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s) 
        counter_t = Counter(t)
        return sum(max(counter_t[key]-counter_s[key],0) for key in counter_t)

# @lc code=end

