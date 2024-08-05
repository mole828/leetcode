#
# @lc app=leetcode id=2053 lang=python3
# @lcpr version=
#
# [2053] Kth Distinct String in an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        # print(counter.keys())
        once = [v for v in arr if counter[v]==1]
        if len(once) < k:
            return ''
        return once[k-1]
# @lc code=end

print(Solution().kthDistinct(["d","b","c","b","c","a"], 2))

#
# @lcpr case=start
# ["d","b","c","b","c","a"]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["aaa","aa","a"]\n1\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","a"]\n3\n
# @lcpr case=end

#

