#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(char*-nfreq for nfreq,char in sorted([(-freq, char) for char, freq in Counter(s).items()]))
    
# @lc code=end

print(Solution().frequencySort('tree'))