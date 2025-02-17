#
# @lc app=leetcode id=1079 lang=python3
# @lcpr version=
#
# [1079] Letter Tile Possibilities
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq_map = Counter(tiles)
        def dfs():
            s = 1
            for k, v in freq_map.items():
                if v == 0:
                    continue
                freq_map[k] -= 1
                s += dfs()
                freq_map[k] += 1
            return s
        return dfs() - 1
# @lc code=end



#
# @lcpr case=start
# "AAB"\n
# @lcpr case=end

# @lcpr case=start
# "AAABBC"\n
# @lcpr case=end

# @lcpr case=start
# "V"\n
# @lcpr case=end

#

