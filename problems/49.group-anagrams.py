#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m: defaultdict[tuple,list[str]] = defaultdict(lambda:[]) 
        for s in strs:
            c = Counter(s)
            m[tuple(sorted(c.items()))].append(s)
        return m.values()
# @lc code=end

print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))