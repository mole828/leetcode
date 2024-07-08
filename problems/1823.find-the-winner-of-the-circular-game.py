#
# @lc app=leetcode id=1823 lang=python3
# @lcpr version=
#
# [1823] Find the Winner of the Circular Game
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        bus = [i for i in range(1, n+1)]
        i = -1
        count = k 
        while len(bus) > 1:
            i += 1
            count -= 1
            i %= len(bus)
            if not count:
                bus.pop(i)
                count = k
                i -= 1
                # print(bus)
        return bus[0]


# @lc code=end

print(Solution().findTheWinner(5,2))
print(Solution().findTheWinner(6,5))

#
# @lcpr case=start
# 5\n2\n
# @lcpr case=end

# @lcpr case=start
# 6\n5\n
# @lcpr case=end

#

