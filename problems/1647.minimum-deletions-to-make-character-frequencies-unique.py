#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        values = counter.values()
        ans = 0
        counter = Counter(values)
        print(counter, ans, set(counter.values()), set([1]))
        while set(counter.values()) != set([1]):
            [(key,value)] = counter.most_common(1)
            d = value - 1
            counter[key] -= d
            counter[key-1] += d
            ans += d
            if key-1 == 0:
                del counter[key-1]
            print(counter, ans, set(counter.values()), set([1]))
        return ans
        
# @lc code=end

