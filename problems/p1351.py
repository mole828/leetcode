from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        y = len(grid) - 1
        x = 0
        while y >= 0:
            ly = len(grid[y])
            while x != ly:
                if grid[y][x] < 0:
                    break
                x += 1
            # print(f"ans+= {n-x}", y, x)
            ans += ly - x
            y -= 1
        return ans