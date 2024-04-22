#
# @lc app=leetcode id=752 lang=python3
# @lcpr version=
#
# [752] Open the Lock
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # def diff(source: str, target: str):
        #     return sum(
        #         abs(int(source[i])-int(target[i]))
        #         for i in range(4)
        #     )
        # print([diff(s,target) for s in deadends])
        def ways(source: str) -> set[str]:
            nums = [int(c) for c in source]
            _ways = set()
            for i in range(4):
                for d in [-1,1]:
                    e = nums.copy()
                    e[i] += d 
                    e[i] %= 10
                    _ways.add(''.join(str(c) for c in e))
            return _ways 
        # print(ways(target))
        que = deque([(0,'0000')])
        visited = set(deadends)
        while que:
            step, comb = que.popleft()
            if comb in visited:
                continue
            visited.add(comb)
            if comb == target:
                return step
            # if comb in deadends:
            #     continue
            for way in ways(comb):
                que.append((step+1, way))
        return -1

# @lc code=end

print(Solution().openLock(["0201","0101","0102","1212","2002"],"0202"))

#
# @lcpr case=start
# ["0201","0101","0102","1212","2002"]\n"0202"\n
# @lcpr case=end

# @lcpr case=start
# ["8888"]\n"0009"\n
# @lcpr case=end

# @lcpr case=start
# ["8887","8889","8878","8898","8788","8988","7888","9888"]\n"8888"\n
# @lcpr case=end

#

