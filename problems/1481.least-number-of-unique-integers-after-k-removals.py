#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        most = Counter(arr).most_common()
        while most and k>=most[-1][1]:
            key,count = most.pop()
            k-=count
        return len(most)
# @lc code=end

print(Solution().findLeastNumOfUniqueInts([5,5,4],1))