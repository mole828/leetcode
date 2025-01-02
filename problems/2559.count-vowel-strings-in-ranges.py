#
# @lc app=leetcode id=2559 lang=python3
# @lcpr version=
#
# [2559] Count Vowel Strings in Ranges
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        START_SET = set(['a', 'e', 'i', 'o', 'u'])
        begins = [(word[0] in START_SET and word[-1] in START_SET)  for word in words]
        sums = [0]
        for i in range(len(words)):
            sums.append(sums[-1] + begins[i])
        res = []
        for query in queries:
            l, r = query
            res.append(sums[r+1] - sums[l])
        return res
        
# @lc code=end



#
# @lcpr case=start
# ["aba","bcb","ece","aa","e"]\n[[0,2],[1,4],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# ["a","e","i"]\n[[0,2],[0,1],[2,2]]\n
# @lcpr case=end

#

