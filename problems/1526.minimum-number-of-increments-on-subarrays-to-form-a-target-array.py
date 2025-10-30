#
# @lc app=leetcode id=1526 lang=python3
#
# [1526] Minimum Number of Increments on Subarrays to Form a Target Array
#

# @lc code=start
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        val2idx = defaultdict(SortedList)
        for i, v in enumerate(target):
            val2idx[v].add(i)
        max_val = max(val2idx.keys())
        ans = 0
        while max_val:
            idxs = val2idx[max_val]
            prev = -2
            for idx in idxs:
                if idx != prev + 1:
                    ans += 1
                prev = idx
                target[idx] -= 1
                val2idx[max_val - 1].add(idx)
            val2idx.pop(max_val)
            max_val -= 1
        return ans
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        last = 0
        for v in target:
            if v > last:
                ans += v - last
            last = v
        return ans
# @lc code=end

