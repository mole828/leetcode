#
# @lc app=leetcode id=2416 lang=python3
# @lcpr version=
#
# [2416] Sum of Prefix Scores of Strings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def prefixs(word):
        for i in range(1, len(word)+1):
            yield word[:i]
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_sum : dict[str, int] = defaultdict(int)
        for word in words:
            for prefix in Solution.prefixs(word):
                prefix_sum[prefix] += 1
        return [sum(prefix_sum[prefix] for prefix in Solution.prefixs(word)) for word in words]
    
# @lc code=end

print([p for p in Solution.prefixs('abc')])

print(Solution().sumPrefixScores(
    ["abc","ab","bc","b"]
))

#
# @lcpr case=start
# ["abc","ab","bc","b"]\n
# @lcpr case=end

# @lcpr case=start
# ["abcd"]\n
# @lcpr case=end

#

