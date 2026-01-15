#
# @lc app=leetcode id=2943 lang=python3
#
# [2943] Maximize Area of Square Hole in Grid
#

# @lc code=start
from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_continue_part(arr: list[int]) -> int:
            window = []
            max_length = 0
            for v in arr:
                if not window or window[-1] == v - 1:
                    window.append(v)
                else:
                    window = [v]
                max_length = max(max_length, len(window))
            return max_length
        hBars.sort()
        if hBars[0] == 1: hBars.pop(0)
        if hBars[-1] == n+2: hBars.pop()
        vBars.sort()
        if vBars[0] == 1: vBars.pop(0)
        if vBars[-1] == m+2: vBars.pop()
        max_h_window = max_continue_part(hBars)
        # print(hBars, max_h_window)
        max_v_window = max_continue_part(vBars)
        # print(vBars, max_v_window)
        return (min(max_h_window, max_v_window)+1) ** 2
                
# @lc code=end

if __name__ == '__main__':
    print(Solution().maximizeSquareHoleArea(3, 2, [3,2,4], [3,2],))