#
# @lc app=leetcode id=2106 lang=python3
# @lcpr version=30204
#
# [2106] Maximum Fruits Harvested After at Most K Steps
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        @cache
        def dfs(pos: int, steps: int, fruits_status: int):
            max_fruits = 0
            for i, (pos_f, amount_f) in enumerate(fruits):
                if fruits_status & (1 << i):
                    continue
                next_fruits_status = fruits_status | (1 << i)
                next_steps = steps + abs(pos - pos_f)
                if next_steps > k:
                    continue
                this_chose = amount_f + dfs(pos_f, next_steps, next_fruits_status)
                max_fruits = max(max_fruits, this_chose)
            return max_fruits
        
        return dfs(startPos, 0, 0)
        
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def get_range(pos: int, left: int) -> tuple[int,int]:
            if left > pos:
                return pos, pos + k
            
            if left < pos - k:
                return pos - k, pos
            
            cost = ( pos - left ) * 2
            left_first = pos + (k - cost)

            cost = pos - left
            right_first = pos + (k - cost) // 2

            return left, max(left_first, right_first, pos)

        fruits.sort()
        max_fruits = 0
        window = []
        window_sum = 0
        last_fruit = fruits.copy()
        for pos_fruits, _ in fruits:
            left, right = get_range(startPos, min(pos_fruits, startPos))
            while last_fruit and last_fruit[0][0] <= right:
                window.append(last_fruit.pop(0))
                window_sum += window[-1][1]
            while window and window[0][0] < left:
                window_sum -= window.pop(0)[1]
            
            max_fruits = max(max_fruits, window_sum)

        return max_fruits
        
# @lc code=end

print(Solution().maxTotalFruits([[2,8],[6,3],[8,6]], 5, 4))

#
# @lcpr case=start
# [[2,8],[6,3],[8,6]]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [[0,3],[6,4],[8,5]]\n3\n2\n
# @lcpr case=end

#

