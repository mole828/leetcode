#
# @lc app=leetcode id=790 lang=python3
# @lcpr version=30204
#
# [790] Domino and Tromino Tiling
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        state = [1, 0, 0, 0]
        mod = 1_000_000_007
        for i in range(1, n + 1):
            new_state = [0] * 4
            new_state[0] = (state[0] + state[1] + state[2] + state[3]) % mod
            new_state[1] = (state[2] + state[3]) % mod
            new_state[2] = (state[1] + state[3]) % mod
            new_state[3] = state[0]
            state = new_state
        return state[0]
        
# @lc code=end

print(Solution().numTilings(3))
print(Solution().numTilings(4))

#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

