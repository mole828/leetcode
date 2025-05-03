#
# @lc app=leetcode id=1007 lang=python3
# @lcpr version=30204
#
# [1007] Minimum Domino Rotations For Equal Row
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def dfs(target: int, index: int, tops: List[int], bottoms: List[int]) -> int:
            if index == len(tops):
                return 0
            if target != tops[index] and target != bottoms[index]:
                return float('inf')
            if target == tops[index]:
                return dfs(target, index + 1, tops, bottoms)
            if target == bottoms[index]:
                return 1 + dfs(target, index + 1, tops, bottoms)
        ans_list = [
            dfs(tops[0], 0, tops, bottoms), 
            dfs(tops[0], 0, bottoms, tops), 
            dfs(bottoms[0], 0, tops, bottoms),
            dfs(bottoms[0], 0, bottoms, tops),
        ]
        print(ans_list)
        ans = min(ans_list)
        if ans == float('inf'):
            return -1
        if ans > len(tops)//2:
            return len(tops) - ans
        return ans
# @lc code=end

print(Solution().minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))

#
# @lcpr case=start
# [2,1,2,4,2,2]\n[5,2,6,2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,2,3]\n[3,6,3,3,4]\n
# @lcpr case=end

#

